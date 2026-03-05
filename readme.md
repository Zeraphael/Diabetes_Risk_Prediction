# Diabetes Risk Prediction

## Project Overview

This project uses machine learning to predict whether a patient is at risk of developing diabetes based on several medical indicators. Early detection of diabetes can help healthcare providers recommend lifestyle changes and treatment to prevent serious complications.

The model analyzes patient health data such as glucose level, body mass index (BMI), age, blood pressure, and insulin levels.

---

## Dataset

The dataset used in this project is the **Diabetes Dataset** from Kaggle.

It contains medical diagnostic measurements collected from female patients of Pima Indian heritage.

### Features in the dataset

* Pregnancies
* Glucose
* Blood Pressure
* Waist Circumference cm
* Insulin
* Body Mass Index (BMI)
* Family History Diabetes 
* Age
* Gender  
* Fasting GlucoseG level
* Cholesterol Level
* Triglycerides Level
* Physical Activity Level   
* Daily Calorie Intake 
* Sugar Intake Grams Per Day
* Sleep Hours 
* Stress Level
* Age


### Target Variable

* **Outcome**

  * 0 → No diabetes
  * 1 → Diabetes risk

---

## Project Workflow

### 1. Data Cleaning

* Checked for missing or invalid values
* Replaced impossible values (such as 0 for glucose or BMI)

### 2. Exploratory Data Analysis (EDA)

* Distribution of medical features
* Correlation between features
* Visualization using charts

### 3. Feature Scaling

* Standardization of numerical variables for better model performance

### 4. Model Training

Machine learning algorithms were trained to predict diabetes risk.

Example models that can be used:

* Logistic Regression
* Random Forest
* K-Nearest Neighbors

### 5. Model Evaluation

Models were evaluated using:

* Accuracy
* Confusion Matrix
* Classification Report

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Project Structure

```
diabetes-risk-prediction/
│
├── diabetes_model.ipynb
├── diabetes.csv
├── app.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Deploy the model as a web application using Streamlit
* Improve model performance with feature engineering
* Add more medical datasets for better prediction

---

## Author

**Biniyam Fenta**

Aspiring Data Scientist with interest in healthcare data science and machine learning.

GitHub: https://github.com/Zeraphael
