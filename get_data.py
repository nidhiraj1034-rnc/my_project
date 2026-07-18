import pandas as pd
import numpy as np

print("Generating offline datasets for Diabetes, Heart Disease, and Lung Cancer...")

np.random.seed(42)
num_samples = 500

# 1. Diabetes Data Generation (8 Features + Outcome)
diabetes_data = pd.DataFrame({
    'Pregnancies': np.random.randint(0, 10, num_samples),
    'Glucose': np.random.randint(70, 200, num_samples),
    'BloodPressure': np.random.randint(60, 120, num_samples),
    'SkinThickness': np.random.randint(10, 50, num_samples),
    'Insulin': np.random.randint(15, 300, num_samples),
    'BMI': np.random.uniform(18, 45, num_samples),
    'DiabetesPedigreeFunction': np.random.uniform(0.1, 2.0, num_samples),
    'Age': np.random.randint(21, 80, num_samples),
    'Outcome': np.random.randint(0, 2, num_samples)
})
diabetes_data.to_csv('diabetes.csv', index=False)

# 2. Heart Disease Data Generation (13 Features + Target)
heart_data = pd.DataFrame({
    'age': np.random.randint(29, 80, num_samples),
    'sex': np.random.randint(0, 2, num_samples),
    'cp': np.random.randint(0, 4, num_samples),
    'trestbps': np.random.randint(94, 200, num_samples),
    'chol': np.random.randint(126, 400, num_samples),
    'fbs': np.random.randint(0, 2, num_samples),
    'restecg': np.random.randint(0, 3, num_samples),
    'thalach': np.random.randint(71, 202, num_samples),
    'exang': np.random.randint(0, 2, num_samples),
    'oldpeak': np.random.uniform(0.0, 6.2, num_samples),
    'slope': np.random.randint(0, 3, num_samples),
    'ca': np.random.randint(0, 5, num_samples),
    'thal': np.random.randint(0, 4, num_samples),
    'target': np.random.randint(0, 2, num_samples)
})
heart_data.to_csv('heart.csv', index=False)

# 3. Lung Cancer Data Generation (8 key parameters + Outcome)
lung_cancer_data = pd.DataFrame({
    'Age': np.random.randint(30, 85, num_samples),
    'Smoking_Habit': np.random.randint(1, 3, num_samples), # 1=No, 2=Yes
    'Yellow_Fingers': np.random.randint(1, 3, num_samples),
    'Anxiety_Level': np.random.randint(1, 3, num_samples),
    'Chronic_Disease': np.random.randint(1, 3, num_samples),
    'Fatigue_Level': np.random.randint(1, 3, num_samples),
    'Wheezing_Issue': np.random.randint(1, 3, num_samples),
    'Coughing_Blood': np.random.randint(1, 3, num_samples),
    'Outcome': np.random.randint(0, 2, num_samples)
})
lung_cancer_data.to_csv('lung_cancer.csv', index=False)

print("Success: diabetes.csv, heart.csv, and lung_cancer.csv generated successfully offline!")