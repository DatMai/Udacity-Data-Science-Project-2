# Disaster Response Pipeline Project

### Motivation for the Project:
The aim of this project was to utilize my skills in data engineering to examine disaster data from Figure Eight and develop an API model that can categorize disaster messages. A machine learning pipeline was constructed to classify real messages that were transmitted during disasters, which enabled them to be sent to the appropriate disaster relief agency. A web application was created as part of the project, which allows emergency workers to input new messages and receive classification results across various categories. Additionally, the web app features data visualizations.

### Descriptions of Files:
app

| - template
| |- master.html # main page of web app
| |- go.html # classification result page of web app
|- run.py # Flask file that runs app

data

|- disaster_categories.csv # data to process
|- disaster_messages.csv # data to process
|- process_data.py # data cleaning pipeline
|- InsertDatabaseName.db # database to save clean data to

models

|- train_classifier.py # machine learning pipeline
|- classifier.pkl # saved model

Notebook

|- categories.csv
|- messages.csv
|- ETL Pipeline Preparation.ipynb
|- ML Pipeline Preparation.ipynb
|-Disaster_Response.db

README.md

### Project Components
This project comprises of three main components that I completed:

1. ETL Pipeline
The first component is a Python script named process_data.py, which is responsible for data cleaning pipeline that:
- Loads the messages and categories datasets
- Merges the two datasets
- Cleans the data
- Stores the cleaned data in a SQLite database
To prepare the process_data.py script, an ETL Pipeline Preparation Jupyter notebook was utilized for EDA.

2. ML Pipeline
The second component is a Python script named train_classifier.py, which is responsible for a machine learning pipeline that:
- Loads data from the SQLite database
- Splits the dataset into training and test sets
- Builds a text processing and machine learning pipeline
- Trains and tunes a model using GridSearchCV
- Outputs results on the test set
- Exports the final model as a pickle file

3. Flask Web Application
As part of this project, I created a Flask web application that allows an emergency worker to input a new message and receive classification results across several categories. Additionally, the web app displays data visualizations. The following are the outputs of the web app:
![image](https://user-images.githubusercontent.com/74104677/230732415-e46d000e-fe1c-44bb-9d15-b9ab46618559.png)
![image](https://user-images.githubusercontent.com/74104677/230732550-b70eca98-7f25-41e8-9185-5d97bd5a689e.png)
![image](https://user-images.githubusercontent.com/74104677/230732590-a209554d-fcde-4ba5-8cb2-92ab76f5fbbe.png)
![image](https://user-images.githubusercontent.com/74104677/230733054-92393b07-f439-4f06-b3b1-bda5050e10c0.png)
![image](https://user-images.githubusercontent.com/74104677/230733075-183dc292-a0b0-43e7-a2d8-fd6a9bc069e9.png)


### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/
