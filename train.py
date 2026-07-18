import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

print("Training Machine Learning Models for Multiple Disease Prediction...")

# Train Diabetes Model
db = pd.read_csv('diabetes.csv')
db_model = RandomForestClassifier(random_state=42)
db_model.fit(db.drop('Outcome', axis=1), db['Outcome'])
pickle.dump(db_model, open('diabetes_model.pkl', 'wb'))

# Train Heart Disease Model
ht = pd.read_csv('heart.csv')
ht_model = RandomForestClassifier(random_state=42)
ht_model.fit(ht.drop('target', axis=1), ht['target'])
pickle.dump(ht_model, open('heart_model.pkl', 'wb'))

# Train Lung Cancer Model
lc = pd.read_csv('lung_cancer.csv')
lc_model = RandomForestClassifier(random_state=42)
lc_model.fit(lc.drop('Outcome', axis=1), lc['Outcome'])
pickle.dump(lc_model, open('lung_cancer_model.pkl', 'wb'))

print("Success: All 3 updated models trained and exported offline successfully!")