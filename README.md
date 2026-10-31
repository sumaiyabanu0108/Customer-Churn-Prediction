# Customer Churn Prediction Using Machine Learning

## Project Overview
This project predicts whether a telecom customer is likely to leave the company (churn) using Machine Learning techniques.

The project includes data preprocessing, exploratory data analysis, model training, model evaluation, and an interactive web application built using Streamlit.

## Objectives
- Analyze customer data to understand churn patterns.
- Preprocess and prepare data for Machine Learning.
- Train and compare multiple classification models.
- Predict customer churn using customer details.
- Display predictions through an interactive web application.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Google Colab

## Machine Learning Models
Two classification algorithms were trained and evaluated:

1. Logistic Regression
2. Random Forest Classifier

### Model Performance

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 80.4% | 78.4% |
| Precision | 64.8% | 62.3% |
| Recall | 57.2% | 47.3% |
| F1 Score | 60.8% | 53.8% |
| ROC-AUC | 83.6% | 81.2% |

Logistic Regression was selected as the final model based on its overall evaluation performance.

## Dataset
The project uses the IBM Telco Customer Churn dataset.

Dataset source:  
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv

## Project Structure
```text
Customer-Churn-Prediction/
│
├── Customer_churn_prediction.ipynb
├── app.py
├── churn_model.pkl
└── README.md
```

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/sumaiyabanu0108/Customer-Churn-Prediction.git
```

### 2. Open the project folder
```bash
cd Customer-Churn-Prediction
```

### 3. Install required libraries
```bash
pip install streamlit pandas scikit-learn==1.6.1 joblib
```

### 4. Run the Streamlit application
```bash
streamlit run app.py
```

### 5. Open the application
Open the local URL shown in your terminal, usually:
`http://localhost:8501`

## Features
- Customer information input
- Machine Learning-based churn prediction
- Churn probability display
- Interactive Streamlit interface

## Future Improvements
- Improve model performance through hyperparameter tuning.
- Add more visualizations.
- Deploy the application online.

## Author
**Sumaiya Banu**

GitHub: https://github.com/sumaiyabanu0108

