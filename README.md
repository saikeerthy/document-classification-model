# document classification model

Data Available:

Heavywater document classification - with 2 columns
1st column - document name
2nd column - document text

Steps followed:

I divided the data into 80-20 split for training and testing, trained the model using random forest classifier, then saved the models to "vectorizer.pkl" and "random_forest.pkl" using joblib. To run it as a local webservice, I created a python file app1.py in which I used flask along with REST API to send the prediction output along with confidence of prediction.

Still in progress:

I am trying to deploy the model to a public cloud platform - AWS. For that I created an s3 bucket named "heavywatermodel" in which I added the two models "vectorizer.pkl" and "random_forest.pkl". I have successfully accessed the files from the bucket and ran the model on local machine. Now, I am currently working on deploying to AWS lambda.

Steps :

I created a folder and Installed virtual environment in that with python 2.7. I have installed all the needed libraries in the virtual environment. In terminal, in the path of the created folder, activate the virtual environment and run app1.py. 

