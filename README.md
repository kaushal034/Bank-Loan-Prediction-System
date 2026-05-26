# Bank-Loan-Prediction-System

#  Project Overview

The Bank Loan Prediction System is a Machine Learning-based application developed to predict whether a customer’s loan application will be approved or rejected based on applicant details and financial information.
Banks receive many loan applications daily, and manual verification takes a lot of time. This project helps automate the loan approval prediction process using Machine Learning algorithms.
The system analyzes customer information such as:
Applicant Income
Coapplicant Income
Education
Employment Status
Loan Amount
Credit History
Property Area
Marital Status
and predicts the loan approval status.

# Problem Statement

Banks need an efficient system to identify eligible customers for loan approval. Manual analysis is time-consuming and may lead to errors.
The goal of this project is to:
reduce manual work,
improve prediction accuracy,and support banking decision-making using machine learning.

# Objectives

Predict loan approval status using customer information.
Perform data preprocessing and cleaning.
Analyze customer financial patterns.
Train a machine learning classification model.
Deploy the prediction system using Streamlit.

# Dataset Information

The dataset contains customer and loan-related information.
Important Features:
Gender
Married
Dependents
Education
Self_Employed
ApplicantIncome
CoapplicantIncome
LoanAmount
Loan_Amount_Term
Credit_History
Property_Area
Target Variable:
Loan_Status
Y = Loan Approved
N = Loan Rejected

#  Technologies Used

Programming Language
Python
Libraries Used
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Pickle
Streamlit

# Project Workflow

1. Import Libraries
Imported all required Python libraries for:
data analysis,
visualization,
machine learning,
and deployment.

2. Load Dataset
Loaded the loan dataset into Pandas DataFrame using CSV file.

Example:
df = pd.read_csv("loan_data.csv")

3. Data Cleaning and Preprocessing
Performed:handling missing values,
duplicate removal,
feature formatting,
and categorical data conversion.
This improved dataset quality before training the model.

4. Handle Missing Values
Some columns contained null values.
Techniques used:
Median filling
Mode filling
This ensured complete and usable data.

5. Exploratory Data Analysis (EDA)
Performed data analysis using:
count plots,
box plots,
histograms,
heatmaps.
EDA helped identify:
customer patterns,
feature relationships,
loan approval trends.

6. Feature Encoding
Categorical features such as:
Gender,
Education,
Property Area
were converted into numerical format using encoding techniques.
Machine learning models require numerical input data.

7. Train-Test Split
Dataset divided into:
80% Training Data
20% Testing Data
Training data helps the model learn patterns, while testing data evaluates performance.

8. Machine Learning Model
Random Forest Classifier
Used Random Forest Classifier for loan approval prediction.
Why Random Forest?
High accuracy
Reduces overfitting
Handles multiple features effectively
Works well for classification problems

9. Model Training
The model was trained using customer financial and personal information.
Example:
model.fit(X_train, y_train)
The model learned patterns from training data and predicted loan approval status.

10. Model Evaluation
Model performance was evaluated using:
Accuracy Score
Confusion Matrix
Classification Report
These metrics helped measure prediction performance and model reliability.

11. Save Model using Pickle
After successful training:
the model was saved as:
model.pkl
Advantages:
reusable model,
faster deployment,
no need to retrain every time.

12. Deployment using Streamlit
The project was deployed using Streamlit to create a user-friendly web application.
Users can:
enter customer details,
click predict,
and get instant loan approval prediction.
Run locally using:
streamlit run app.py

# Features of the Application

Real-time Loan Prediction
User-friendly Interface
Machine Learning-based Analysis
Fast and Automated Prediction
Streamlit Web Application

# Model Output
The model predicts:
Loan Approved
or
Loan Rejected
based on customer input details.

#  Real-World Applications

Banking Systems
Financial Institutions
Loan Approval Automation
Credit Risk Analysis
Customer Eligibility Screening

#  Conclusion

This project demonstrates how Machine Learning can automate and improve the loan approval prediction process. The system helps banks and financial institutions make faster and more accurate decisions using customer financial data and predictive analytics.

This project demonstrates how Machine Learning can automate and improve the loan approval prediction process. The system helps banks and financial institutions make faster and more accurate decisions using customer financial data and predictive analytics.
