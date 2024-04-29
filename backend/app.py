import numpy as np
import torch
import pandas as pd
import os, sys
from disease_pred import load_model, GeneticData, CrohnsPred
from data_functions import format_vcf, format_txt, to_dataframe, fill_missing_mutations

from flask import Flask, redirect, request, jsonify, json, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app=app)

FILE = []
dir = '../data/user_file'

# user data
def get_prediction(file):
    try:
        filetype = 0
        grCh_ls = pd.read_csv('causal_grCh_liftover.txt', sep='\t')  # reference genome alignment liftover
        print('Copying File:')
        # check if filetype is accepted
        if str(file.filename).endswith('.txt'):
            file_dir = dir + '.txt'
            filetype = 1
            print('Filetype: .txt')
        elif str(file.filename).endswith('.vcf'):
            file_dir = dir + '.vcf'
            filetype = 2
            print('Filetype: .vcf')
        elif str(file.filename).endswith('.vcf.gz'):
            file_dir = dir + '.vcf.gz'
            filetype = 2
            print('Filetype: .vcf.gz')
        else: 
            print('Filetype not accepted:') # any other filetype
            return (-1, -1, [])
        file.save(file_dir)
        print('Analysing File:')
        try:
            if filetype == 2:
              (data, found, snp_by_chrom, manual_prs) = format_vcf(file_dir, grCh_ls) # if vcf
            elif filetype==1:
                (data, found, snp_by_chrom, manual_prs) = format_txt(file_dir, grCh_ls) # if txt
            print('File done.')
        except:
            os.remove(file_dir) # immediately remove file from directory if error arises
            print('File unreadable. Removed.')
            return (-1, -1, [])
        os.remove(file_dir)  # immediately remove file from directory after processing is complete
        print('File removed.')
        filled_data = fill_missing_mutations(data, found, grCh_ls) # set gt of missing SNPs to 0
        mut_list = list(grCh_ls['RSID'])
        df = to_dataframe(filled_data, mut_list)
        print('Analysis done.')
        data = GeneticData(df) # create Dataset instance
        input_geno = data.__getitem__() # get formatted sample info
        model = load_model() # load model from saved path
        print('Model loaded.')
        with torch.no_grad():
            score = model(input_geno)
        print('All Finished. Responding to frontend.')
        return (float(score), manual_prs, snp_by_chrom) # return NN score, manual PRS and snp-by-chromosome array
    except:
        print('An error occurred.')
        return (-1, -1, [])
    
# handle file upload from frontend    
@app.route('/pred', methods=["GET", "POST"])
def get_file():
    response_object = {}
    if request.method == "POST": # handle file upload from frontend
        uploaded_file = request.files['file']
        FILE.append(uploaded_file.filename)
        (score, manual_prs, snp_by_chrom) = get_prediction(uploaded_file) # start analysis
        print(score, manual_prs, snp_by_chrom)
        if score == -1: # handle any error during file analysis
            response_object['result'] = 'The uploaded file is in the wrong format. Please upload a valid genotype file.'
            response_object['status'] = -1
        else: # if processing is successful
            response_object['status'] = 1
            response_object['result'] = str(score)
            response_object['prs'] = str(manual_prs)
            response_object['user_snps'] = snp_by_chrom
    
    else: # handle 'get' request onload
        response_object['file'] = FILE
        response_object['status'] = 0
        response_object['result'] = 'Awaiting File.'
        response_object['prs'] = 0
        response_object['user_snps'] = []
    return response_object



# test data
def analyse_test_file(file_dir):
    try: # filetype check not necessary
        grCh_ls = pd.read_csv('causal_grCh_liftover.txt', sep='\t') # reference genome alignment liftover
        print('Analysing File:')
        (data, found, snp_by_chrom, manual_prs) = format_txt(file_dir, grCh_ls) # if txt
        print('File done.')
        filled_data = fill_missing_mutations(data, found, grCh_ls)
        mut_list = list(grCh_ls['RSID'])
        df = to_dataframe(filled_data, mut_list)
        print('Analysis done.')
        data = GeneticData(df)
        input_geno = data.__getitem__() # if txt
        model = load_model()
        print('Model loaded.')
        with torch.no_grad():
            score = model(input_geno)
        print('All Finished. Responding to frontend.')
        return (float(score), manual_prs, snp_by_chrom)
    except: # handle any unforseen error
        print('An error occurred.')
        return (-1, -1, [])    
    
# handle analysis of built-in test data
@app.route('/pred-testfile', methods=["GET"]) 
def pred_sample_file():
    response_object = {}
    print('GET Request')
    uploaded_file = '../data/testfile.txt'
    FILE.append('testfile')
    (score, manual_prs, snp_by_chrom) = analyse_test_file(uploaded_file)
    print(score, manual_prs, snp_by_chrom)
    if score == -1: 
        response_object['result'] = 'An error occurred. Please retry.'
        response_object['status'] = -1
    else:
        response_object['status'] = 1
        response_object['result'] = str(score)
        response_object['prs'] = str(manual_prs)
        response_object['user_snps'] = snp_by_chrom
    return response_object


@app.route('/')
def home():
    # redirect to prediction page
    return redirect('/pred')
    
if __name__ == "__main__":
    app.run(debug=True) # remove after dev build