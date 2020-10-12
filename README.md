# CP4D-bank
# Description
This demo aims to automate the banking experience for customers regarding loans on Cloud Pak for Data using Watson Studio, Watson Knowledge Catalog, & Watson Assistant. The project is currently built on the cloud, this documentation aims to provide step-by-step details to implement the same on CP4D on any infrastructure.
### Features
- User can interact with the system using a web application or through Watson Assistant
- Watson Assistant can answer the following questions (our plans):
  - Queries about loans (Loan Predicition, recommending loans and tips to be eligible for loans)
  - History transactions
- Two ML models:
  - Loan Prediction model, using Auto AI, to predict user eligibility for loan
  - Recommendation system, python notebook, recommend specific loans for users and how to be eligible for loan
# Collect
In this project we are using German credit data set: https://online.stat.psu.edu/stat857/node/215/
# Organize
# Analyze 
# Infuse



# Steps

Step 1
1. We found a German credit data set: https://online.stat.psu.edu/stat857/node/215/
2. We decided to go with the Cloud Pak for Data as a service (Watson Studio). This will help us connect Watson Assistant to our service later. We also provisioned Watson Knowledge Catalog (because we will be using the personal info of the user), Watson Machine Learning and DB2 instance.
3. We uploaded the data set to Watson Studio. 
