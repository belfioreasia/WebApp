# CrohnsPred: Deep Neural Network For Crohn Disease (CD) Prediction
A user-friendly web application for your genetic risk score of Crohn's Disease!\
Visit [this repository](https://github.com/belfioreasia/CrohnsPred) for the CrohnsPred model for Genetic Risk prediction of Crohn's Disease.


## Requirements
The project is written in `python`. The following third party packages are required to ensure full project functionality:

* torch >= 2.2
* pandas
* numpy
* flask
* npm
* vue.js 3 
* vue-cli
* axios
* Chart.js
* d3.js
* bootstrap
* babel
* gsap

All necessary imports, libraries and modules are specified at [_frontend/package.json_](frontend/package.json) and [_frontend/package-lock.json_](frontend/package-lock.json) file.

## Example Usage

### 1. DOWNLOAD THIS REPOSITORY
Download all the files in this repository into a local directory '__WebApp__' and keep the same directory structure.

### 2. START BACKEND
Open two terminals at the '__WebApp__' directory.\
On one run __cd backend__.\
Then run __python app.py__ or __python3 app.py__ based on your python version. This activates the backend!

### 3. START FRONTEND
On one other terminal run __cd frontend__.\
Then run __npm run serve__ or __npm run dev__. This activates the frontend!

### 4. GET YOUR PREDICTION!
* Open a web page at [__http://localhost:8080/__](http://localhost:8080/), and test our website!


## Data

To enable prediction, the input *.vcf* data must include:
- Chromosome (column 'chrom'): an Integer
- Position (column 'pos'): an Integer
- SNP name (column 'rsid' or 'ID'): as a string 'rsXXYY...'
- Reference Allele (column 'ref'): a character (A/C/T/G) or string
- ALternative Allele (column 'alt'): a character (A/C/T/G) or string

The model output will contain a value in the range [0,1], wether a higher risk has not been detected or otherwise. 


## Authors

- Belfiore Asia (*ec21414*)
    
    CID:210471618\
    BSc Computer Science and Mathematics,
    Queen Mary University of London
