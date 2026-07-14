from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('LoanApprovalModel.pkl', 'rb'))
print(model.feature_names_in_)
print(model.n_features_in_)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    education = 1 if request.form['education'] == "Graduate" else 0
    employment_status = (
        1 if request.form['employment_status'] in ["Employed", "Salaried"]
        else 0
    )
    co_applicant = 1 if request.form['co_applicant'] == "Yes" else 0

    annual_income = float(request.form['annual_income'])
    monthly_expenses = float(request.form['monthly_expenses'])
    credit_score = float(request.form['credit_score'])
    loan_amount = float(request.form['loan_amount'])
    loan_term = float(request.form['loan_term'])
    warning = ""
    if annual_income < 20009 or annual_income > 149998:
        warning += "⚠️ Annual Income is outside the training range.<br>"

    if monthly_expenses < 500 or monthly_expenses > 4999:
        warning += "⚠️ Monthly Expenses are outside the training range.<br>"

    if credit_score < 300 or credit_score > 849:
        warning += "⚠️ Credit Score is outside the training range.<br>"

    if loan_amount < 5000 or loan_amount > 44848:
        warning += "⚠️ Loan Amount is outside the training range.<br>"

    if loan_term < 12 or loan_term > 239:
        warning += "⚠️ Loan Term is outside the training range.<br>"
    # Feature engineering
    savings = annual_income - (monthly_expenses * 12)
    loan_income_ratio = loan_amount / annual_income
    estimated_emi = loan_amount / loan_term

    input_data = pd.DataFrame(
        [[
            education,
            employment_status,
            co_applicant,
            annual_income,
            monthly_expenses,
            credit_score,
            loan_amount,
            loan_term,
            savings,
            loan_income_ratio,
            estimated_emi
        ]],
        columns=[
            'Education',
            'Employment_Status',
            'Co-Applicant',
            'Annual_Income',
            'Monthly_Expenses',
            'Credit_Score',
            'Loan_Amount_Requested',
            'Loan_Term',
            'Savings',
            'Loan_Income_Ratio',
            'Estimated_EMI'
        ]
    )

    # ⚠️ IMPORTANT: must match training order EXACTLY


    print(input_data)

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1] * 100

    if prediction == 1:
        result = f"✅ Loan Approved (Approval Probability: {prob:.2f}%)"
    else:
       result = f"❌ Loan Rejected (Rejection Probability: {(100 - prob):.2f}%)"
    return render_template(
        'index.html',
        prediction=result,
        warning=warning
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)