import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, mean_squared_error, r2_score
import joblib

# Load dataset
df = pd.read_csv("us_army_explosive_dissolution_data.csv")

# Encode features
le = LabelEncoder()
df['Material_encoded'] = le.fit_transform(df['Material'])
df['Risk_Level_encoded'] = df['Risk_Level'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Prepare data
features = ['Temperature_C', 'Surface_Area_cm2', 'Mixing_Speed_rpm', 'pH_Level', 'Material_encoded']
X = StandardScaler().fit_transform(df[features])
y_class = df['Risk_Level_encoded']
y_reg = df['Dissolution_Rate_mg_min']

# Split for classification
X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)
clf = RandomForestClassifier().fit(X_train, y_train)
print("Classifier Report:\n", classification_report(y_test, clf.predict(X_test)))

# Split for regression
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y_reg, test_size=0.2, random_state=42)
reg = RandomForestRegressor().fit(X_train_r, y_train_r)
y_pred_r = reg.predict(X_test_r)
print("Regressor R²:", r2_score(y_test_r, y_pred_r))

# Save models
joblib.dump(clf, "risk_classifier_model.pkl")
joblib.dump(reg, "dissolution_regressor_model.pkl")
joblib.dump(StandardScaler().fit(df[features]), "feature_scaler.pkl")