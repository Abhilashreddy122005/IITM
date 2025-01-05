from flask import Flask, request, jsonify
from sentiment_analysis import get_sentiment
from geolocation import get_location
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib 


model = joblib.load("random_forest_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Credit Risk Assessment"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    
    income = data['income']
    credit_score = data['credit_score']
    sentiment = get_sentiment(data['user_name'])  # from social media sentiment
    latitude, longitude = get_location(data['address'])

   
    feature_vector = [income, credit_score, sentiment, latitude, longitude]
    
    
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform([feature_vector])

    
    prediction = model.predict(scaled_features)

    
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
