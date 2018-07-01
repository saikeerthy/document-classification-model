# document classification model

Data Available:

Heavywater document classification - with 2 columns
1st column - document name
2nd column - document text

Steps followed:

I divided the data into 80-20 split for training and testing, trained the model using random forest classifier, then saved the models to "vectorizer.pkl" and "random_forest.pkl" using joblib. To run it as a local webservice, I created a python file app1.py in which I used flask along with REST API to send the prediction output along with confidence of prediction.

Still in progress:

I am trying to deploy the model to a public cloud platform - AWS. For that I created an s3 bucket named "heavywatermodel" in which I added the two models "vectorizer.pkl" and "random_forest.pkl" but It is giving me an error S3ResponseError: 301 - MovedPermanently. 

