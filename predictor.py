import numpy as np
import pandas as pd
import textstat
import joblib

# Load model and vectorizer
model = joblib.load("Models/ai_detector_model.pkl")
vectorizer = joblib.load("Models/vectorizer.pkl")

def calculate_readability(text):
    """Calculate readability score for the text"""
    return textstat.flesch_reading_ease(text)

def lexical_diversity(text):
    """Compute lexical diversity = unique words / total words"""
    words = text.split()
    return len(set(words)) / len(words) if words else 0

def sentence_length(text):
    """Compute average sentence length"""
    sentences = text.split('.')
    return sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0

def preprocess_text(text):
    """Convert text to feature vectors (TF-IDF + readability metrics)"""
    
    # Convert input text into a DataFrame
    df_sample = pd.DataFrame({'text': [text]})

    # Extract additional features
    df_sample['readability'] = df_sample['text'].apply(calculate_readability)
    df_sample['lexical_diversity'] = df_sample['text'].apply(lexical_diversity)
    df_sample['sentence_length'] = df_sample['text'].apply(sentence_length)

    # Convert text to TF-IDF vector
    X_tfidf = vectorizer.transform(df_sample['text'])

    # Combine TF-IDF features with extracted features
    X_sample = np.hstack((X_tfidf.toarray(), 
                          df_sample[['readability', 'lexical_diversity', 'sentence_length']].values))

    return X_sample

def predict_text(text):
    X_sample = preprocess_text(text)
    prediction = model.predict(X_sample)[0]
    confidence = model.predict_proba(X_sample)[:,1][0] 
    return prediction, confidence
