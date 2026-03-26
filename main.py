import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

nltk.download('punkt')

def summarize_text(text, top_n=2):
    sentences = sent_tokenize(text)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    scores = np.sum(X.toarray(), axis=1)
    top_indices = scores.argsort()[-top_n:]
    summary = [sentences[i] for i in sorted(top_indices)]
    return summary

if __name__ == "__main__":
    with open("sample.txt", "r") as file:
        text = file.read()

    summary = summarize_text(text, top_n=3)

    print("\n--- SUMMARY ---\n")
    for line in summary:
        print(line)
