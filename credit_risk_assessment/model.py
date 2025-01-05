import pandas as pd
import shap
from sklearn.preprocessing import StandardScaler


data = {
    'income': [40000, 50000, 60000],
    'credit_score': [650, 700, 750],
    'sentiment_score': [0.1, -0.3, 0.5],
    'geolocation_lat': [28.6139, 19.0760, 51.5074],
    'geolocation_lon': [77.2090, 72.8777, -0.1278],
    'utility_payment_frequency': [1, 0, 1]
}

df = pd.DataFrame(data)


scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import xgboost as xgb


y = [0, 1, 0] 


X_train, X_test, y_train, y_test = train_test_split(df_scaled, y, test_size=0.2, random_state=42)

models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'XGBoost': xgb.XGBClassifier(),
    'SVM': SVC(),
    'Naive Bayes': GaussianNB()
}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{model_name}:\n", classification_report(y_test, y_pred))
import shap


explainer = shap.TreeExplainer(models['Random Forest'])
shap_values = explainer.shap_values(X_test)

shap.summary_plot(shap_values, X_test)
