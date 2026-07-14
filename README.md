#Loan Approval Prediction System

A Machine Learning-based Loan Approval Prediction System developed using Python, Flask, and Scikit-learn. The application predicts whether a loan application is likely to be approved based on applicant information such as income, expenses, credit score, loan amount, and loan term.

## Features

- Predicts loan approval using Machine Learning
- User-friendly Flask web interface
- Feature engineering for improved prediction
- Random Forest Classifier model
- Input validation for user entries
- Real-time prediction

## Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS
- Bootstrap
- Pickle

## Dataset

The dataset contains applicant information including:

- Education
- Employment Status
- Co-Applicant
- Annual Income
- Monthly Expenses
- Credit Score
- Loan Amount Requested
- Loan Term

## Machine Learning Models Evaluated

The following machine learning models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- XGBoost Classifier

After comparing their performance, the **Random Forest Classifier** was selected for deployment.

**Final Deployed Model:** Random Forest Classifier

**Accuracy:** 85.58%

## Project Structure

```
Loan_Approval_Project/
│── app.py
│── Loan Approval.ipynb
│── LoanApprovalModel.pkl
│── Loan Dataset.csv
│── requirements.txt
│── templates/
│── static/
```

## Installation

1. Install the required libraries

```bash
pip install -r requirements.txt
```

2. Run the application

```bash
python app.py
```

3. Open your browser and visit

```
http://127.0.0.1:5000/
```

## Future Improvements

- Deploy the application on Render
- Improve prediction accuracy
- Add more applicant features
- Enhance UI and user experience
## Live Demo
https://loan-approval-system-1-ffgp.onrender.com
## Author

**Saurav Kumar**
B.Tech Civil Engineering(4th Year), NIT Warangal
