# 📈 Bank Marketing Success Predictor

https://utkarsh-s-prophecy.streamlit.app/


## 📋 Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
  - [Key Variables](#key-variables)
- [Features](#features)
- [Modeling Pipeline](#modeling-pipeline)
  - [Workflow](#workflow)
  - [Best Model](#best-model)
- [Performance](#performance)
  - [Feature Importance](#feature-importance)
- [Streamlit Web App](#streamlit-web-app)
  - [How to Run](#how-to-run)
- [License](#license)

---

## 🧐 Overview
The **Bank Marketing Success Predictor** is a machine learning project designed to forecast the success of direct marketing campaigns conducted by a banking institution. The goal is to predict whether a client will subscribe to a term deposit ("yes" or "no") based on client demographics and past interactions.

---

## 📊 Dataset
The dataset includes details about client interactions, demographics, and marketing campaign results. 

### Files:
- **Training Set**: `train.csv`
- **Test Set**: `test.csv`

### Key Variables
#### 🎯 Target Variable
- **Target**: Whether the client subscribed to a term deposit (binary: "yes", "no").

#### 🔢 Input Features
1. **Last Contact Date**: Date of last contact.
2. **Age**: Age of the client (numeric).
3. **Job**: Type of job (categorical).
4. **Marital**: Marital status (categorical: "married", "divorced", "single").
5. **Education**: Education level (categorical: "primary", "secondary", "tertiary").
6. **Default**: Has credit in default? (binary: "yes", "no").
7. **Balance**: Average yearly balance in euros (numeric).
8. **Housing**: Has a housing loan? (binary: "yes", "no").
9. **Loan**: Has a personal loan? (binary: "yes", "no").
10. **Contact**: Type of communication (categorical: "cellular", "telephone").
11. **Duration**: Duration of the last contact in seconds (numeric).
12. **Campaign**: Number of contacts during this campaign (numeric).
13. **Pdays**: Days since last contact from a previous campaign (numeric; -1 indicates no prior contact).
14. **Previous**: Number of prior contacts (numeric).
15. **Poutcome**: Outcome of the previous campaign (categorical).

---

## 🛠 Features
Data preprocessing includes:
- **Numerical Features**: Handled using scaling and missing value imputation.
- **Categorical Features**: One-hot encoding for categorical variables.

Pipeline steps:
1. Handle missing data.
2. Scale numerical features.
3. Encode categorical features.

---

## 🤖 Modeling Pipeline
### Workflow
1. Preprocessing using column transformers.
2. Model training using:
   - **Logistic Regression**
   - **Random Forest**
   - **Gradient Boosting**
3. Hyperparameter tuning with GridSearchCV.
4. Evaluation on validation data using accuracy and F1-score.

### Best Model
- **Gradient Boosting Classifier**:
  - Validation F1-score: `0.472`
  - Hyperparameters: Learning rate = `0.1`, Estimators = `200`

---

## 📈 Performance
- **Public F1-score**: `0.70178`
- The model emphasizes key features like **contact duration**, **balance**, and **campaign details**.

### 🔍 Feature Importance
Top features include:
- Contact duration
- Campaign details
- Balance

---

## 🌐 Streamlit Web App
The project includes a **Streamlit web application** for user interaction.

### Key Features
1. **Upload Data**: Upload a dataset to get predictions.
2. **Modify Inputs**: Change feature values to see how predictions change.
3. **Visualize Results**: View feature importance and prediction results interactively.

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bank-marketing-predictor.git
