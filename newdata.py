# 🔧 Required Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Step 1: Load Dataset
df = pd.read_csv('synthetic_explosive_dissolution_data.csv')  # Replace with your file path if needed

# 📊 Step 2: Initial Overview
print("🔹 Dataset Shape:", df.shape)
print("🔹 First 5 rows:\n", df.head())
print("🔹 Column Info:\n", df.dtypes)

# 🔍 Step 3: Check for Missing Values
print("\n🧪 Missing Values:\n", df.isnull().sum())

# 📈 Step 4: Visualize Feature Distributions
numerical_features = ['Temperature_C', 'Surface_Area_cm2', 'Mixing_Speed_rpm', 'pH_Level', 'Dissolution_Rate_mg_min']


# 📌 Step 5: Encode Categorical Features
# Encode 'Material' using LabelEncoder
le = LabelEncoder()
df['Material_encoded'] = le.fit_transform(df['Material'])

# Map Risk_Level to numeric for classification
risk_map = {'Low': 0, 'Medium': 1, 'High': 2}
df['Risk_Level_encoded'] = df['Risk_Level'].map(risk_map)

# 🔄 Step 6: Normalize Numerical Features
scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[numerical_features] = scaler.fit_transform(df[numerical_features])

# 📦 Step 7: Final Cleaned Dataset for Modeling
processed_df = df_scaled[['Material_encoded'] + numerical_features + ['Risk_Level_encoded']]
print("✅ Final Preprocessed Data:\n", processed_df.head())

# 💾 Step 8: Save Preprocessed Data (optional)
processed_df.to_csv("preprocessed_explosive_data.csv", index=False)
print("📁 Saved preprocessed dataset as 'preprocessed_explosive_data.csv'")
