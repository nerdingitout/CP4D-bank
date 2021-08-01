#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import requests

def main(dict):
    # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
    API_KEY = dict["api_key"]
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {
	"input_data": [
		{
			"fields": [
				"Gender",
				"Married",
				"Dependents",
				"Education",
				"Self_Employed",
				"ApplicantIncome",
				"CoapplicantIncome",
				"LoanAmount",
				"Loan_Amount_Term",
				"Credit_History",
				"Property_Area"
			],
			"values": [
				[
					dict["gender"],
					dict["married"],
					dict["dependents"],
					dict["education"],
					dict["self_employed"],
					dict["applicantIncome"],
					dict["coapplicantIncome"],
					dict["loan_amount"],
					dict["loan_amount_term"],
					dict["credit_history"],
					dict["housing"]
				]
			]
		}
	]
}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/39f83fe3-b2c2-4401-b70e-9229da48f179/predictions?version=2021-07-14', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print("Scoring response")
    print(response_scoring.json())
    
    return { 'message': response_scoring.json() }
