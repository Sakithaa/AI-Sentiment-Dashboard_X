
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tweepy
import config

def main():
    client = tweepy.Client(bearer_token=config.TWITTER_BEARER_TOKEN)
    query = " OR ".join(config.KEYWORDS)

    try:
        response = client.search_recent_tweets(
            query=query,
            max_results=100,
            tweet_fields=["text", "created_at"]
        )

        if response.data:
            for tweet in response.data:
                print(f"{tweet.created_at} - {tweet.text}\n")
        else:
            print("No tweets found for your keywords.")

    except Exception as e:
        print(f"Error fetching tweets: {e}")

if __name__ == "__main__":
    main()
