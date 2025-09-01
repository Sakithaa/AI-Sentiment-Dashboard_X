import os
import re
import pandas as pd
from langdetect import detect, LangDetectException
from deep_translator import GoogleTranslator
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# --------- Functions ---------
def clean_tweet_text(text):
    text = re.sub(r'RT\s@\w+:|@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def translate_to_english(text):
    try:
        if len(text.strip()) > 10:
            lang = detect(text)
            if lang != 'en':
                return GoogleTranslator(source='auto', target='en').translate(text)
        return text
    except LangDetectException:
        return text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def label_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# --------- Paths relative to script location ---------
script_dir = os.path.dirname(os.path.abspath(__file__))  # this folder = Project/scripts
input_file = os.path.join(script_dir, 'tweets.txt')      # tweets.txt should be in scripts/
output_file = os.path.join(script_dir, 'cleaned_sentiment_tweets.csv')

# --------- Read & Process Tweets ---------
try:
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f" File not found: {input_file}")
    exit()

data = []
for line in lines:
    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\+\d{2}:\d{2}) - (.*)', line)
    if match:
        timestamp = match.group(1)
        tweet = match.group(2).strip().replace('"', '')
        cleaned = clean_tweet_text(tweet)
        if cleaned:
            translated = translate_to_english(cleaned)
            data.append({'time': timestamp, 'tweet': translated})

if not data:
    print(" No valid tweets processed.")
    exit()

df = pd.DataFrame(data)

# --------- Sentiment Analysis ---------
sia = SentimentIntensityAnalyzer()
df['compound'] = df['tweet'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['pos'] = df['tweet'].apply(lambda x: sia.polarity_scores(x)['pos'])
df['neu'] = df['tweet'].apply(lambda x: sia.polarity_scores(x)['neu'])
df['neg'] = df['tweet'].apply(lambda x: sia.polarity_scores(x)['neg'])
df['sentiment_label'] = df['compound'].apply(label_sentiment)

# --------- Save CSV ---------
df.to_csv(output_file, index=False)
print(f" Done! CSV saved to {output_file}")
