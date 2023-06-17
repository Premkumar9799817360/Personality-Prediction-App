# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w2sfeOIa1RNkdu_NIb1I2fwIYHLit1VM
"""

from flask import Flask, render_template, request, jsonify,redirect
from sklearn.feature_extraction.text import CountVectorizer
#from flask_ngrok import run_with_ngrok
import pickle
import nltk
# nltk.download('stopwords')
# nltk.download('wordnet')
app = Flask(__name__)

model0 = pickle.load(open('iemodel.pkl','rb'))
model1 = pickle.load(open('nsmodel.pkl','rb'))
model2 = pickle.load(open('ftmodel.pkl','rb'))
model3 = pickle.load(open('pjmodel.pkl','rb'))
model4 = pickle.load(open('CountVectorizer.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict')
def predict(): 
    text = request.args.get('text')
    text = model4.transform([text])
    ie = model0.predict(text)
    ns = model1.predict(text)
    ft = model2.predict(text)
    pj = model3.predict(text)
    # prediction = ie[0]+ns[0]+ft[0]+pj[0]
    # print(prediction)
    prediction = ""
    if ie[0]=='I':
      prediction+="Introvert\n"
    else:
      prediction+="Extrovert\n"
    if ns[0]=='N':
      prediction+="Intuition\n"
    else:
      prediction+="Sensing\n"
    if ft[0]=="F":
      prediction+="Feeling\n"
    else:
      prediction+="Thinking\n"
    if pj=="P":
      prediction+="Preceiving\n"
    else:
      prediction+="Judging"
    # return render_template('index.html', OUTPUT= '{}'.format((prediction)))
    return render_template('index.html',prediction_text = f" {prediction}")

if __name__ == "__main__":
    app.run(debug=True)
