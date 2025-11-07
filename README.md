### Real-Time Public Sentiment Dashboard (Twitter/X)

## Objective
The goal of this project is to track public opinion about AI in real-time using Twitter (X) data. The pipeline extracts tweets, cleans them, applies sentiment analysis, and visualizes results in a live interactive dashboard.

## Tools & Libraries
- Python: Tweepy (API), Pandas, NLTK (Sentiment), LangDetect, Deep Translator
- Visualization: Streamlit, Altair
- Environment: Virtual Environment (venv)

## Data Collection
- Created a Twitter/X Developer Account and generated:
1. Bearer Token
2. Access Token & Secret
3. API Keys
- Used Tweepy to query tweets using the keyword “AI” (brand/product focus).
- Since a free account has limitations (restricted tweet volume), I extracted around 50 tweets and saved them into a text file (tweets.txt).
- These tweets serve as the dataset for cleaning, analysis, and visualization.

## Project Workflow
# 1.Tweet Extraction
- Python script connects to Twitter API and extracts tweets related to AI.
- Tweets are stored in tweets.txt.

# 2. Data Cleaning & Sentiment Analysis
- Removed noise (hashtags, mentions, links, emojis).
- Non-English tweets were translated into English (using deep-translator).
- Applied NLTK VADER sentiment analyzer to generate sentiment scores (pos, neg, neu, compound).
- Added sentiment labels: Positive / Negative / Neutral.
- Saved output as cleaned_sentiment_tweets.csv.

# 3. Dashboard (Visualization)
- Built using Streamlit + Altair.
- Components:
    - Sentiment Distribution (bar chart)
    - Hourly Average Sentiment Trend (line chart)
    - Summary Metrics (average sentiment, total tweets, % distribution)
- Run with:
    streamlit run scripts/3.streamlit_sentiment_dashboard.py


## Usage
- Create & Activate Environment
python -m venv Py_Env
Py_Env\Scripts\activate

- Install Dependencies
pip install -r requirements.txt

- Run Pipeline
Extract tweets:
python scripts/1.stream_tweets.py
(or use already saved tweets.txt)

- Clean & analyze sentiment:
python scripts/2.cleaning_and_sentiment.py

- Launch dashboard:
streamlit run scripts/3.streamlit_sentiment_dashboard.py

## Deliverables
- Live Sentiment Dashboard (Streamlit)
- Python Streaming + NLP Scripts
- Processed Dataset (cleaned_sentiment_tweets.csv)
- Explanation of workflow + code

## Limitations
- Used a free Twitter Developer Account, so only limited tweets could be extracted.
- Extracted around 50 tweets about AI (static dataset).
- Could not enable real-time continuous streaming due to free account restrictions.
- Daily logs not implemented because the dataset is static.
- Despite limitations, the project simulates a real-time sentiment tracking system for AI discussions on Twitter.

## Live Dashboard
- View the Live Dashboard here - https://ai-sentiment-dashboardx-q6spuwne5zwjmvs2f56cvj.streamlit.app/
