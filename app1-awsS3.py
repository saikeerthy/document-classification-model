from flask import Flask,render_template,request, jsonify
import numpy as np
from sklearn.externals import joblib
import pickle
import pandas as pd
import os
import boto
from boto.s3.key import Key

# feature vectors path
#VECTORIZER_PATH = "models/vectorizer.pkl"
# final model path
#MODEL_PATH = "random_forest.pkl"

BUCKET_NAME = 'heavywatermodel'
prefix = 'templates/'

PREP_FILE_NAME = 'vectorizer.pkl'
PREP_LOCAL_PATH = PREP_FILE_NAME

MODEL_FILE_NAME = 'random_forest.pkl'
MODEL_LOCAL_PATH = MODEL_FILE_NAME

HTML_FILE_NAME = 'upload.html'
HTML_LOCAL_PATH = MODEL_FILE_NAME

AWS_S3_HOST = 's3.eu-west-1.amazonaws.com'

#os.mkdir('templates')


if not os.path.exists('templates'):
    os.mkdir('templates')

app = Flask(__name__)


@app.route('/')
def my_form():
    load_model()
    return render_template(file_html)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    
    #processed_text = text.upper()
    s = [text]
    d = { 'data':s}
    kf = pd.DataFrame.from_dict(d)
    xx = kf.data
    asa = vectorizer.transform(xx)
    result = final_model.predict(asa)
    return str(result)

def load_model():
    global vectorizer
    global final_model
    global file_html
    
    conn = boto.connect_s3('ACCESS ID ','SECURITY KEY')
    bucket = conn.get_bucket(BUCKET_NAME)
    key_obj = Key(bucket)


    key_obj.key = PREP_FILE_NAME
    contents = key_obj.get_contents_to_filename(PREP_LOCAL_PATH)# vectorize function
    vectorizer = joblib.load(PREP_LOCAL_PATH)
    
    key_obj.key = MODEL_FILE_NAME # random forest
    contents = key_obj.get_contents_to_filename(MODEL_LOCAL_PATH) # random forest
    final_model = joblib.load(MODEL_LOCAL_PATH)

    
    key_obj.key = HTML_FILE_NAME
    contents = key_obj.get_contents_to_filename('templates/' + HTML_FILE_NAME)# vectorize function
    file_html = HTML_FILE_NAME

if __name__ == "__main__":
    app.run(debug = True)






