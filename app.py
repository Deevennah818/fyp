import streamlit as st
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load the pre-trained model and vectorizer using joblib
best_rf = joblib.load(r'C:\Users\Dee\OneDrive - Asia Pacific University\Desktop\fyp dataset\best_random_forest_model.pkl')
vectorizer = joblib.load(r'C:\Users\Dee\OneDrive - Asia Pacific University\Desktop\fyp dataset\tfidf_vectorizer.pkl')

# Initialize stopwords and lemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Preprocess the input text
def preprocess_text(text):
    text = text.lower()
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])
    return text

# Streamlit form layout for user input (like the flight delay prediction system)
with st.form("news_form"):
    st.header("Fake News Detection System")
    
    # Input fields for the form
    article_title = st.text_input("Enter the Title of the News Article")
    article_content = st.text_area("Enter the Content of the News Article")
    
    # Submit button
    submit_button = st.form_submit_button("Predict")

if submit_button:
    # Preprocess the article content
    processed_content = preprocess_text(article_content)
    
    # Vectorize the content
    vectorized_text = vectorizer.transform([processed_content]).toarray()
    
    # Make the prediction
    prediction = best_rf.predict(vectorized_text)
    
    # Display the prediction
    if prediction == 1:
        st.write("🚨 This is Fake News! 🚨")
    else:
        st.write("✅ This is Real News. ✅")

