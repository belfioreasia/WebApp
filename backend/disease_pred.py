# ALL imports
import torch  
import numpy as np
from torch import nn
import pandas as pd 

path = 'model/crohns_pred.pth'


# Load model ----------------------------------------------------------------------------------------------------------

def load_model():
    model = torch.load(path)
    model.eval()
    print(model)
    return model

# MODEL -----------------------------------------------------------------------------------------------------------
""" Neural Network for PRS Prediction:
       -  
       -  
"""
# MODEL -----------------------------------------------------------------------------------------------------------
class CrohnsPred(nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.input_size = input_size

        # input layer ---------------------[ input size: num_mutations = 140 --> input size: num_mutations = 140 ] 
        self.input_layer = nn.Linear(input_size, input_size)
        # (8) hidden layers ------------[ input size: num_mutations --> output size: CD snps = 140 (h1), chromosome pairs = 22* (h2) ] 
        self.hidden1 = nn.Linear(input_size, input_size)
        self.hidden2 = nn.Linear(input_size, input_size)
        self.hidden3 = nn.Linear(input_size, input_size)
        self.hidden4 = nn.Linear(input_size, input_size)
        self.hidden5 = nn.Linear(input_size, input_size)
        self.hidden6 = nn.Linear(input_size, input_size)
        self.hidden7 = nn.Linear(input_size, input_size)
        self.hidden8 = nn.Linear(input_size, input_size)
        self.hidden9 = nn.Linear(input_size, input_size)
        self.hidden10 = nn.Linear(input_size, 22)
        self.hidden11 = nn.Linear(22, 22)
        self.hidden12 = nn.Linear(22, 22)
        self.hidden13 = nn.Linear(22, 22)
        self.hidden14 = nn.Linear(22, 22)
        self.hidden15 = nn.Linear(22, 22)
        self.hidden16 = nn.Linear(22, 22)
        self.hidden17 = nn.Linear(22, 22)
        self.hidden18 = nn.Linear(22, 22)
        self.hidden19 = nn.Linear(22, 22)
        self.hidden20 = nn.Linear(22, 22)
        self.output_layer = nn.Linear(22, 1) # output layer -----[ input size: 4 --> output size: prediction score = 1 ] 

        self.dropout = nn.Dropout(p=0.1) # dropout layer
        # activation functions #
        self.relu = nn.PReLU(1)  # for hidden layers 
        self.sigmoid = nn.Sigmoid()  # for output layer 

    # model forward pass flow
    def forward(self, x):
        # ReLU activation for input and hidden layers #
        x = self.relu(self.input_layer(x)) 
        x = self.relu(self.hidden1(x)) 
        x = self.relu(self.hidden2(x)) 
        x = self.relu(self.hidden3(x)) 
        x = self.relu(self.hidden4(x))
        x = self.relu(self.hidden5(x)) 
        x = self.relu(self.hidden6(x)) 
        x = self.relu(self.hidden7(x)) 
        x = self.relu(self.hidden8(x)) 
        x = self.relu(self.hidden9(x)) 
        x = self.dropout(x)   # dropout layer
        x = self.relu(self.hidden10(x)) 
        x = self.relu(self.hidden11(x)) 
        x = self.relu(self.hidden12(x)) 
        x = self.relu(self.hidden13(x)) 
        x = self.relu(self.hidden14(x)) 
        x = self.relu(self.hidden15(x)) 
        x = self.relu(self.hidden16(x)) 
        x = self.relu(self.hidden17(x)) 
        x = self.relu(self.hidden18(x)) 
        x = self.relu(self.hidden19(x)) 
        x = self.relu(self.hidden20(x)) 
        x = self.output_layer(x)
        x = self.sigmoid(x) # squash output between 0 and 1
        return x
    
    def xavier_init(self, m):
        if type(m) == nn.Linear:
            torch.nn.init.xavier_uniform_(m.weight)
    

# DATA -------------------------------------------------------------------------------------------------------------
""" Dataset for Genomic Variants Data --> final training dataset format: 
       - the file dataset.txt contains the list of SNPs per sample ID [columns 1-129], and PRS value per sample [last column] 
       - train dataset was split from the original dataset [10% of the entire dataset] 
"""
class GeneticData(torch.utils.data.Dataset):
    """ Dataset for Genomic Variants Data """

    def __init__(self, file_df):
        """ Args --> file (String) = Directory to the .txt file with the data
        """
        self.data = file_df
        print(file_df)
        self.num_mutations = self.data.shape[1]
        print(self.num_mutations)
        cols = self.data.columns.tolist()
        self.sample = file_df[cols[0]]
        self.genotypes = self.data.loc[:, cols[1]:cols[self.num_mutations-1]]

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self):
        x = self.genotypes.iloc[0].tolist()
        x = torch.tensor(np.float32(x))
        return x