# 🧠 Personality Type Prediction using NLP  

This project aims to classify users into **16 MBTI (Myers-Briggs Type Indicator)** personality types (e.g., **INTJ, ENFP**) based on their social media text data. It leverages **Natural Language Processing (NLP)** and **Machine Learning** techniques to understand personality patterns from linguistic behavior.

---

## 🌐 **Live Demo**

🎯 **Try it out here:**  
[![Live Streamlit App](https://img.shields.io/badge/Open%20App-Live%20Demo-brightgreen?style=for-the-badge&logo=streamlit)](https://personality-prediction-app.onrender.com/)

---

## 📊 **About the Dataset**

- **Dataset Name:** [MBTI Personality Types 500 Dataset on Kaggle](https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset)  
- **Records:** ~106,000 preprocessed social media posts  
- **Features:**
  - `type` → MBTI personality label (e.g., INTP, ESFJ)
  - `posts` → Text data from user posts  
- **Dataset Structure:**  
  The dataset is **balanced** across the 16 MBTI personality types to ensure diverse and unbiased model training.  
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset?utm_source=chatgpt.com)

---

## 🧩 **Understanding MBTI Dichotomies**

The MBTI categorizes individuals based on four key dimensions:  

| Dichotomy | Description |
|------------|-------------|
| **Introversion (I)** vs **Extraversion (E)** | Focus of attention (inner world vs outer world) |
| **Sensing (S)** vs **Intuition (N)** | How information is perceived |
| **Thinking (T)** vs **Feeling (F)** | How decisions are made |
| **Judging (J)** vs **Perceiving (P)** | Approach to the external world |

Each person is classified into **one of 16 personality types**, based on the combination of these preferences.

![Screenshot (40)](https://github.com/Premkumar9799817360/Personality-Prediction-App/assets/83695512/1419e651-f7e2-4f74-9541-7151f91d8cea)



🔗 **References:**  
[Health.com](https://www.health.com/personality-type-7969612?utm_source=chatgpt.com) | [Kaggle](https://www.kaggle.com/datasets/zeyadkhalid/mbti-personality-types-500-dataset) | [GeeksforGeeks](https://www.geeksforgeeks.org/mbti-personality-types/)

---

## 🧪 **Data Preprocessing Pipeline**

Steps followed to clean and prepare data for ML models:

1. **Text Cleaning:**  
   - Removed punctuation, stopwords, URLs, emojis, and non-alphabetic characters.  
2. **Tokenization:**  
   - Split posts into tokens using `NLTK` or `spaCy`.  
3. **Vectorization:**  
   - Applied **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert text into numerical vectors.  
4. **Label Encoding:**  
   - Encoded 16 MBTI types as categorical labels for model training.  
5. **Train-Test Split:**  
   - Divided data (80% training / 20% testing).

---

## 🤖 **Machine Learning Models Implemented**

| Model | Description | Key Strength |
|--------|--------------|---------------|
| **Multinomial Naive Bayes** | Probabilistic model based on Bayes' theorem | Simple, fast, and works well with text data |
| **Random Forest** | Ensemble of decision trees | Reduces overfitting and increases stability |
| **Support Vector Classifier (SVC)** | Finds the best hyperplane for classification | Effective in high-dimensional spaces |

✅ **Model Training:**  
All models were trained on the preprocessed TF-IDF data. Hyperparameters were tuned using `GridSearchCV` for best accuracy.

---
![Screenshot (40)](https://github.com/Premkumar9799817360/Personality-Prediction-App/assets/83695512/1419e651-f7e2-4f74-9541-7151f91d8cea)

![Screenshot (41)](https://github.com/Premkumar9799817360/Personality-Prediction-App/assets/83695512/2911afef-efa8-43a0-9490-884e800af817)
