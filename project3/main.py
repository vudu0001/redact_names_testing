import glob
from itertools import chain
import nltk
from nltk.corpus import wordnet
#nltk.download("wordnet")
#nltk.download("omw-1.4")
import os
import regex as re
import spacy
import sys
import warnings
warnings.filterwarnings("ignore")

nlp=spacy.load("en_core_web_sm")
input_files=[]
output = {}

def Read_file(path):
    idata=[]
    files=list(chain.from_iterable(path))

    for i in range(len(files)):
        finput=glob.glob(files[i])
        for j in range(len(finput)):
            dat=open(finput[j]).read()
            idata.append(dat)
            #print(idata)
            input_files.append(finput[j])
    return idata

def redact_names_with(token):
    if token.ent_iob!=0 and token.ent_type_=='PERSON':
        return '\u2588'
    return str(token)

def redact_names(nlp_doc):
    tokens=map(redact_names_with, nlp_doc)
    return ' '.join(tokens)

# Function for Reading Names

def Redact_names(idata):
    tdata=[]
    for text in idata:
        doc=nlp(text)
        tdata.append(redact_names(doc))
    #print(tdata)
    ncount=tdata[0].count('\u2588')
    #print(tdata,ncount)
    output['Names:']=ncount
    #print('namecount: ', ncount)
    return tdata,ncount

def write_output(idata,directory):
    outputfiles=[]
    for i in input_files:
        newname=i
        newname=newname +'.redacted'
        outputfiles.append(newname)

    # Parent Directory path
    parent_dir=str(os.getcwd())
    # Path
    path=os.path.join(parent_dir,directory)
    try:
        os.mkdir(path)
    except:
        print("Directory Exists")

    for i in range(len(outputfiles)):
        despath=str(os.getcwd())+"/"+directory+"/"+outputfiles[i]
        with open(despath, 'w+' , encoding='utf-8') as file:
            file.write(idata[i])
            file.close()
