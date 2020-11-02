# CP4D-bank
## Description
This demo aims to automate the banking experience for customers regarding loans on Cloud Pak for Data using Watson Studio, Watson Knowledge Catalog, & Watson Assistant. The project is currently built on the cloud, this documentation aims to provide step-by-step details to implement the same on CP4D on any infrastructure.
### Features
- User can interact with the system using a web application or through Watson Assistant
- Watson Assistant can answer the following questions (our plans):
  - Queries about loans (Loan Predicition, recommending loans and tips to be eligible for loans)
  - History transactions
- Two ML models:
  - Loan Prediction model, using Auto AI, to predict user eligibility for loan
  - Recommendation system, python notebook, recommend specific loans for users and how to be eligible for loan
## Demo
Demo is currently in progress but can be found <a href="https://cpd-intelligent-loan-agent-app-masa-anam.eu-gb.mybluemix.net/">here</a> and the assistant can be found <a href="https://web-chat.global.assistant.watson.cloud.ibm.com/preview.html?region=us-south&integrationID=a8294af6-dad3-4c5a-b847-669240a31e82&serviceInstanceID=9735eb72-41b7-4552-9b39-aa1badb7e835">here</a>.
## Collect
In this project we are using German credit data set: https://online.stat.psu.edu/stat857/node/215/
<!-- ## Organize
## Analyze 
## Infuse
-->


# Steps

### Step 1
1. We found a German credit data set: https://online.stat.psu.edu/stat857/node/215/
2. We decided to go with the Cloud Pak for Data as a service (Watson Studio). This will help us connect Watson Assistant to our service later. We also provisioned Watson Knowledge Catalog (because we will be using the personal info of the user), Watson Machine Learning and DB2 instance.
3. We uploaded the data set to Watson Studio.
4. Built Auto AI Experiment for Loan Prediction. Works with 0.81 accuracy, results are good so far.
5. Deployed Auto AI on WML (current deployment name: hgjhhjjmhjhkjhkjhk)

### Step 2
1. We built a recommendation system based of the notebook: https://github.com/IBM/product-recommendation-with-watson-ml
2. In the notebook we edited the first 2 sections to have our data set. 
3. In the prepare data section, we added an ID column to our data. 
4. We are using the columns: 
5. 

### Step 3
In this step we mainly focused on building the Loan Assistant with Watson Assistant. Skill can be found in the "loan-skill.json" file.<br>
The assistant can do the following:
- Predict whether user is eligible for loans by asking them a series of questions and then passing into Cloud functions to get results based on the auto ai model we built earlier.
- Recommend Loans for users based on their data.
- Users can apply for loans if they are eligible or can ask more information about how to apply for loan or check required documents.
- Help users with general FAQ questions about loans.
