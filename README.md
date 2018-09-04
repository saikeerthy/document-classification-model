# document classification model
HeavyWater Machine Learning Problem

Problem Statement:

We process documents related to mortgages, aka everything that happens to originate a mortgage that you don't see as a borrower. Often times the only access to a document we have is a scan of a fax of a print out of the document. Our system is able to read and comprehend that document, turning a PDF into structured business content that our customers can act on.
This dataset represents the output of the OCR stage of our data pipeline. Since these documents are sensitive financial documents we have not provided you with the raw text that was extracted. Instead we have had to obscure the data. Each word in the source is mapped to one unique value in the output. If the word appears in multiple documents then that value will appear multiple times. The word order for the dataset comes directly from our OCR layer, so it should be roughly in order.

Here is a sample line:

CANCELLATION NOTICE,641356219cbc f95d0bea231b ... [lots more words] ... 52102c70348d b32153b8b30c

The first field is the document label. Everything after the comma is a space delimited set of word values.
The dataset is present here:

https://drive.google.com/open?id=1JBnFsxb-FmHfvFZuOyhfML_oT-sSBx5X


Mission:

Train a document classification model. Deploy your model to a public cloud platform (AWS/Google/Azure/Heroku) as a webservice.

Data Available:

Heavywater document classification - with 2 columns
1st column - document name
2nd column - document text

Steps followed:

I divided the data into 80-20 split for training and testing, trained the model using random forest classifier, then saved the models to "vectorizer.pkl" and "random_forest.pkl" using joblib. To run it as a local webservice, I created a python file app1.py in which I used flask along with REST API to send the prediction output along with confidence of prediction.

Still in progress:

I am trying to deploy the model to a public cloud platform - AWS. For that I created an s3 bucket named "heavywatermodel" in which I added the two models "vectorizer.pkl" and "random_forest.pkl" and "upload.html" file. I have successfully accessed the files from the bucket and ran the model on local machine. Now, I am currently working on deploying to AWS lambda.

Steps :

I created a folder and Installed virtual environment in that with python 2.7. I have installed all the needed libraries in the virtual environment. In terminal, in the path of the created folder, activate the virtual environment and run app1.py. 

