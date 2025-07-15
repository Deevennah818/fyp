from flask import Flask, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the Flask application
app = Flask(__name__)

# Load the trained Random Forest model
model = joblib.load('best_random_forest_model.pkl')

# Load the TF-IDF vectorizer used during training
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return "Welcome to the Fake News Prediction API!"

# Endpoint to predict if news is fake or not
@app.route('/predict', methods=['POST'])
def predict():
    # Get the news content from the request
    data = request.get_json()

    # Ensure the data contains the 'text' field
    if 'text' not in data:
        return jsonify({'error': 'No text field in the request'}), 400

    text = data['text']
    
    # Convert the text to a TF-IDF vector
    text_tfidf = vectorizer.transform([text])

    # Make a prediction using the model
    prediction = model.predict(text_tfidf)

    # Return the result as JSON
    result = 'Fake' if prediction[0] == 1 else 'Not Fake'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')