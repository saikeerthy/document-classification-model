from flask import Flask,render_template,request, jsonify
import numpy as np
from sklearn.externals import joblib
import pickle
import pandas as pd
import os

# feature vectors path
Vectorizer = "models/vectorizer.pkl"
# final model path
Model = "random_forest.pkl"

app = Flask(__name__)

@app.route('/')
def my_form():
    global vectorizer
    global final_model
    vectorizer = joblib.load(Vectorizer)
    final_model = joblib.load(Model)
    return render_template('upload.html')

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
    resu2 = final_model.predict_proba(asa)
    result2 = np.max(resu2,axis = 1)
    return jsonify({'doc':str(result),'conf':str(result2)})

if __name__ == "__main__":
    app.run(debug = True)






