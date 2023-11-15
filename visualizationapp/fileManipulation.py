import pandas as pd
import seaborn as sns
from django import forms
from . import settings

def handle_uploaded_file(f):
    print("***********************")
    print(f.name)
    print("***********************")
    with open(settings.MEDIA_ROOT, f.name, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def fileUpload(filename, fileType, delimiter): 

    if fileType == "csv" or fileType == "txt" :
        data = pd.read_csv(filename, delimiter=delimiter)
    elif fileType == "xlsx" :
        data = pd.read_excel(filename)
    return data

def getHead(file) :
    return file.head()

def getTail(file) :
    return file.tail()

def getLine(file, lineNumber) :
    return file.loc[lineNumber, :]

def getColumn(file, columnNumber) :
    return file.loc[:, columnNumber]