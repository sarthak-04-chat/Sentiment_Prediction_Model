import streamlit as st
import joblib


model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("tfidf.pkl")
encoder = joblib.load("encoder.pkl")


st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="😊",
    layout="centered"
)


st.title("😊 Sentiment Analysis App")
st.write("Enter a sentence below to predict its emotion.")


user_input = st.text_area(
    "Enter your text",
    height=150,
    placeholder="Example: I am feeling very happy today!"
)


if st.button("Predict Emotion"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")

    else:
        
        text_vector = vectorizer.transform([user_input])

        # Predict emotion
        prediction = model.predict(text_vector)[0]
        emotion = encoder.inverse_transform([prediction])[0]

        # Prediction probability
        confidence = model.predict_proba(text_vector).max() * 100

        st.success(f"### Predicted Emotion: **{emotion.upper()}**")
        st.info(f"Confidence: **{confidence:.2f}%**")