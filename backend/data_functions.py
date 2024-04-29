# ALL imports
import torch
import io
import timeit
import pysam   # for VCF handling
import cyvcf2 # for VCF handling
from cyvcf2 import VCF # for VCF handling
import numpy as np  
import pandas as pd   


#  Format the reference dataset from VCF (in .txt or .vcf/.vcf.gz) to final format for the Neural Network input.
#         - input multipsample vcf filepath: "data/samples/synth_files.vcf.gz" 
#         - output default filepath: "data/dataset.txt"
#         - requirements: reference vcf file with chosen reference samples

# in .txt format
def format_txt(txt_filepath, grCh_ls):
    # Filtered mutations
    print('opening file:', txt_filepath)
    file = open(txt_filepath, 'r')
    print('done.\nReading lines:')
    rows = file.readlines()
    print('done.')
    found = []
    data = {}
    snp_by_chrom = [0 for _ in range(22)] # store number of found mutations on each chromosome
    manual_prs = 0
    header = []
    i = 0
    gt_index = 0
    n = 0
    while n in range(len(rows)):
        row = rows[n]
        if not row.startswith('##'): # iterate through each mutation (and skip headers)
            row = row.split("\t", -1)
            if i==0:
                if row[0].startswith('#'):
                    print('Reading header:')
                    header = row 
                else: 
                    print('preset header') # some VCF files have missing headers, if so use the Dante Labs present VCF header
                    header = ["#CHROM","POS","ID","REF","ALT","QUAL","FILTER","INFO","FORMAT","User"]
                    n = n-1 # re analyze first row
                i=1
                gt_index = len(header)-1
                data['SAMPLE'] = header[gt_index].replace('\n', '')
                print('done.')
            else:
                user_pos = 'chr' + row[0] + ':' + row[1] 
                beta = 0
                # perform alignment liftover if needed
                try:
                    rsid = list(grCh_ls[grCh_ls['grCh37']==user_pos]['RSID'])[0] #grCh37
                    beta = list(grCh_ls[grCh_ls['grCh37']==user_pos]['BETA'])[0] #grCh37
                except:
                    try:
                        rsid = list(grCh_ls[grCh_ls['grCh38']==user_pos]['RSID'])[0] #grCh38
                        beta = list(grCh_ls[grCh_ls['grCh38']==user_pos]['BETA'])[0] #grCh38
                    except:
                        rsid = None
                if (rsid is not None):
                    curr_snp_chr = int(row[0])
                    snp_by_chrom[curr_snp_chr-1] += 1
                    found.append(rsid)
                    print('Found ' + str(len(found)) + ' snps.')
                    gt = row[gt_index][:3]  # sample's alt allele count from genotype field (GT=x/y, with x=0/1/2/... 
                                            # and ref=0, alt=1/2/...)
                    alt_freq = int(gt[0]) + int(gt[2])
                    data[rsid] = [alt_freq]
                    manual_prs += (alt_freq*beta)
                if len(found)==147: break
        n += 1
    return (data, found, snp_by_chrom, manual_prs)


# in .vcf/.vcf.gz format
def format_vcf(vcf_filepath, grCh_ls):
    # Filtered mutations
    print('opening file:', vcf_filepath)
    file = VCF(vcf_filepath)
    print('done.')
    found = []
    snp_by_chrom = [0 for _ in range(22)] # store number of found mutations on each chromosome
    manual_prs = 0
    data = {}
    data['SAMPLE'] = file.samples[0]
    print('Analysing mutations.')
    for rec in file:   # iterate through each mutation 
        curr_snp_chr = (str(rec.CHROM).replace('chr', ''))
        user_pos = 'chr' + str(curr_snp_chr)+':'+str(rec.end) 
        # perform alignment liftover if needed
        try:
            rsid = list(grCh_ls[grCh_ls['grCh37']==user_pos]['RSID'])[0] #grCh37
            beta = list(grCh_ls[grCh_ls['grCh37']==user_pos]['BETA'])[0] #grCh37
        except:
            try:
                rsid = list(grCh_ls[grCh_ls['grCh38']==user_pos]['RSID'])[0] #grCh38
                beta = list(grCh_ls[grCh_ls['grCh38']==user_pos]['BETA'])[0] #grCh38
            except:
                rsid = None
        if (rsid is not None):
            print('mutations found: ', str(len(found))) # track found mutations to terminal
            found.append(rsid)
            snp_by_chrom[int(curr_snp_chr)-1] += 1
            # sample's alt allele count from genotype (GT) field (GT=x/y, with x=0/1/2/...  and ref=0, alt=1/2/...)
            gt = (str(rec.gt_types))    
            # NB: cyvcf2's genotype field describes genotypes as follows:
            #    - 0 --> homozygous ref (0/0) --> encode as 0
            #    - 1 --> heterozygous alt (1/0 or 0/1) --> encode as 1
            #    - 2 --> unknown ref (unknown read on one strand, eg. 0/., ./1) --> encode as 1 (heterozygous alt)
            #    - 3 --> homozygous alt (1/1) --> encode as 2
            alt_freq = int(gt[1])
            if alt_freq >= 2: # adapt genotype reads for cases 2-3
                alt_freq-=1
            data[rsid] = [alt_freq]
            manual_prs += (alt_freq*beta)
        if len(found)==147: break

    return (data, found, snp_by_chrom, manual_prs)


# based on the N mutations found in the file, set athe genotype 
# of all missing 147-N mutations to 0 and return the updated dictionary
# This assumes that missing genotypes are treated as non-mutated alleles
def fill_missing_mutations(vcf_dict, found, grCh_ls):
    mut_list = list(grCh_ls['RSID'])
    for snp in mut_list:
        if snp not in found:
            vcf_dict[snp]=[0] # add gt=0 for non found mutations
    return vcf_dict


# transform the dictionary to a dataframe for the creation of a 
# GeneticData instance for model prediction
def to_dataframe(vcf_dict, columns):
    ordered_dict = {}
    ordered_dict['SAMPLE'] = vcf_dict['SAMPLE'] 
    # ensure the file mutations follow the order of the model training and test data
    for col in columns:
        ordered_dict[col] = vcf_dict[col]
    dataset = pd.DataFrame(ordered_dict)
    # dataset.set_index('SAMPLE', inplace=True)
    return dataset