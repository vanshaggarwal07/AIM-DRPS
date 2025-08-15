import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset
df = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset
print(df.head())

# Drop rows with missing values
df.dropna(inplace=True)

# Alternatively, fill missing values with the mean
df.fillna(df.mean(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Example: Encoding a categorical column 'Category'
le = LabelEncoder()
df['Category'] = le.fit_transform(df['Category'])

# Standardize numerical columns
scaler = StandardScaler()
df[['Feature1', 'Feature2']] = scaler.fit_transform(df[['Feature1', 'Feature2']])

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_data.csv', index=False)

# Example: Splitting features and target
X = df.drop('Target', axis=1)
y = df['Target']

# Optionally, split into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
