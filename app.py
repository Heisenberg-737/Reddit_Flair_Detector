import praw
import json
import numpy as np
import flask
import joblib
from flask import Flask, render_template, request, jsonify
import re
import pandas as pd
import requests
import csv
import time
import datetime
import sys
import sklearn.linear_model
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import unicodedata
from bs4 import BeautifulSoup

reddit=praw.Reddit(client_id='RD4BIpMTGlTVgw', client_secret='_X6Xr7GZom9JNZ6wkLg_twa6L6M',
username='pkothari_17', password='reddit101', user_agent='Reddit Flair',)

#flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
    predict()


#Text Pre-Processing
def strip_html_tags(text):
    
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text(separator=" ")
    return stripped_text


def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


def normalizeString(s):
    s = unicodeToAscii(s.lower().strip())
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-Z.!?]+", r" ", s)
    return s


def remove_whitespace(text):
    text = text.strip()
    return " ".join(text.split())


def string_form(value):
    return str(value)


def text_preprocessing(text):
    text = strip_html_tags(text)
    text = remove_whitespace(text)
    text = normalizeString(text)
    text = text.lower()
    text = string_form(text)

    return text

#def deleted_text(text):
    #if(text=="nan" or text=="NaN" or text=="[removed]" or text=='[deleted]'):
        #text=" "

@app.route('/predict',methods=['POST'])
def predict():

    url = request.form['link']
    submission=reddit.submission(url=url)
    
    title=submission.title
    flair= submission.link_flair_text

    title_cleaned=text_preprocessing(title)

    #title_cleaned = deleted_text(title_cleaned)
    #flair = deleted_text(flair)    
    X=title_cleaned
    
    loaded_model = joblib.load('finalized_model.sav')
    
    prediction = loaded_model.predict(X.split(" "))
    output = prediction[0]

    return render_template('home.html', prediction='{}'.format(output), prediction1= '{}'.format(flair))

def predict_text(url,new_model):


    submission=reddit.submission(url=url)

    title=submission.title
    flair= submission.link_flair_text

    title_cleaned=text_preprocessing(title)

    #title_cleaned = deleted_text(title_cleaned)
    #flair = deleted_text(flair)    
    X=title_cleaned

    prediction = new_model.predict(X.split(" "))

    output = prediction[0]
    return format(output)


#Endpoint
@app.route('/automated_testing',methods=['POST'])
def automated_testing():
	try:
		r = request.files['upload_file']
		url=r.readlines()

		key=[]
		value=[]

		loaded_model = joblib.load('finalized_model.sav')

		for i in range(0,len(url)):
			a=url[i].decode("utf-8")
			val=predict_text(a,loaded_model)
			key.append(a)
			value.append(val)

		dic={"Key":key,"Value":value}
		print(dic)
		return jsonify(dic)

	except:
		return 'Please upload correct file format.'

if __name__ == "__main__":
    
    app.run(debug=True)