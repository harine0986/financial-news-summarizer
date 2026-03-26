# Financial News Summarizer

This project summarizes financial news articles using NLP techniques.

## Features
- Extractive summarization using TF-IDF
- Sentence ranking based on importance
- Simple Streamlit UI

## How it Works
1. Splits text into sentences
2. Converts sentences into TF-IDF vectors
3. Ranks sentences based on importance
4. Selects top sentences as summary

## Run Instructions

### Install dependencies
pip install -r requirements.txt

### Run in terminal
python main.py

### Run Web App
streamlit run app.py
