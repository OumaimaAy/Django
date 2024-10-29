# reclamation/utils.py
from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Define categories based on polarity score
    if polarity > 0.5:
        return "Very Positive"
    elif 0.1 < polarity <= 0.5:
        return "Positive"
    elif -0.1 <= polarity <= 0.1:
        return "Neutral"
    elif -0.5 <= polarity < -0.1:
        return "Negative"
    else:
        return "Very Negative"