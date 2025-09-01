# streamlit_sentiment_dashboard.py
# 30 days Tasks\Project\scripts> streamlit run 3.streamlit_sentiment_dashboard.py
import os
import streamlit as st
import pandas as pd
import altair as alt

# --------- Page Config ---------
st.set_page_config(page_title="Twitter Sentiment Dashboard", layout="wide")
st.title(" Twitter/X Sentiment Dashboard")

# --------- Loading Data ---------
#  the path relative to the script, so it always works
script_dir = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(script_dir, "cleaned_sentiment_tweets.csv")

try:
    df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
    st.error(f"File not found: {DATA_FILE}")
    st.stop()

#  'time' column is datetime
df['time'] = pd.to_datetime(df['time'])

# --------- 🔹 Metrics Here ---------
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Tweets", len(df))

with col2:
    st.metric("Average Sentiment", round(df['compound'].mean(), 3))

# --------- 🔹 Sentiment % Distribution ---------
st.subheader("Sentiment Overview (%)")

total = len(df)
sentiment_percent = df['sentiment_label'].value_counts(normalize=True) * 100

col3, col4, col5 = st.columns(3)

with col3:
    st.metric("Positive %", f"{sentiment_percent.get('Positive', 0):.1f}%")

with col4:
    st.metric("Neutral %", f"{sentiment_percent.get('Neutral', 0):.1f}%")

with col5:
    st.metric("Negative %", f"{sentiment_percent.get('Negative', 0):.1f}%")


# --------- 1️ Sentiment Counts ---------
st.subheader("Sentiment Distribution")
sentiment_counts = df['sentiment_label'].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']

bar_chart = alt.Chart(sentiment_counts).mark_bar().encode(
    x='sentiment',
    y='count',
    color='sentiment'
).properties(width=600, height=400)

st.altair_chart(bar_chart)

# --------- 2️ Sentiment Trend Over Time (Hourly) ---------
st.subheader("Hourly Average Sentiment Trend")
hourly_sentiment = df.groupby(df['time'].dt.hour)['compound'].mean().reset_index()
hourly_sentiment.columns = ['hour', 'avg_sentiment']

line_chart = alt.Chart(hourly_sentiment).mark_line(point=True).encode(
    x='hour:O',
    y='avg_sentiment:Q'
).properties(width=800, height=400)

st.altair_chart(line_chart)


