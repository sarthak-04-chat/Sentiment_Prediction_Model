# 📊 Sentiment Analysis Using Machine Learning

A Machine Learning-based **Sentiment Analysis** project that classifies text into different emotions using **Natural Language Processing (NLP)** techniques. The project uses **TF-IDF Vectorization** for feature extraction and a **Logistic Regression** model for emotion prediction. The trained model is deployed using **Streamlit** to provide real-time predictions through a user-friendly web interface.

---

## 🚀 Project Overview

This project analyzes textual data and predicts the underlying emotion expressed in a sentence. It follows a complete Machine Learning workflow including data preprocessing, feature extraction, model training, model serialization, and deployment.

The application enables users to enter any text and instantly receive the predicted emotion.

---

## ✨ Features

- Text preprocessing and cleaning
- Emotion classification using Machine Learning
- TF-IDF Vectorization
- Logistic Regression model
- Interactive Streamlit web application
- Fast real-time predictions
- Saved model using Joblib

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib
- Jupyter Notebook

---

## 📂 Project Structure

```
Sentimental-Analysis/
│
├── frontend.py
├── NLP project.ipynb
├── emotion_model.pkl
├── tfidf.pkl
├── encoder.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

1. Load the dataset
2. Preprocess and clean text
3. Convert text into TF-IDF vectors
4. Train the Logistic Regression model
5. Save the trained model using Joblib
6. Build the Streamlit web application
7. Predict emotions from user input

---

## 🧹 Text Preprocessing

The following preprocessing techniques were applied:

- Convert text to lowercase
- Remove punctuation
- Remove numbers
- Remove special characters
- Remove stopwords
- Tokenization
- Text normalization

---

## 🤖 Machine Learning Model

**Feature Extraction**
- TF-IDF Vectorizer

**Classification Algorithm**
- Logistic Regression

**Model Serialization**
- Joblib

---

## 💻 Streamlit Web Application

The application allows users to:

- Enter any sentence
- Click the **Predict Emotion** button
- Instantly receive the predicted emotion

### Example

**Input**

```
I am feeling very happy today.
```

**Output**

```
Predicted Emotion: Joy
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/sarthak-04-chat/Sentimental-Analysis.git
```

### Navigate to the project folder

```bash
cd Sentimental-Analysis
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run frontend.py
```

---

## 📋 Requirements

```
streamlit
scikit-learn
pandas
numpy
nltk
joblib
```

---

## 🎯 Applications

- Social Media Sentiment Analysis
- Customer Feedback Analysis
- Product Review Classification
- Opinion Mining
- Chatbots
- Mental Health Monitoring

---

## 🔮 Future Enhancements

- Deep Learning models (LSTM/BERT)
- Multi-language support
- Emotion confidence score visualization
- Voice-based sentiment analysis
- Interactive dashboard
- Model performance comparison

---

## 📸 Project Demo

Users can:

- Enter text into the application
- Click the **Predict Emotion** button
- View the predicted emotion instantly

