import pandas as pd
from ntscraper import Nitter
from datetime import datetime, timedelta

# List of Twitter accounts to scrape
twitter_accounts = [
    "Mr_Derivatives",
    "warrior_0719",
    "ChartingProdigy",
    "allstarcharts",
    "yuriymatso",
    "TriggerTrades",
    "AdamMancini4",
    "CordovaTrades",
    "Barchart"
]

scraper = Nitter()
final_tweets = []

# Loop through each Twitter account
for account in twitter_accounts:
    tweets = scraper.get_tweets(account, mode='user', number=50)
    for tweet in tweets['tweets']:
        data = [tweet['text'], tweet['date']]
        final_tweets.append(data)

# Create DataFrame from collected tweets
data = pd.DataFrame(final_tweets, columns=['text', 'date'])

# Convert date strings to datetime
data['date'] = pd.to_datetime(data['date'], format='%b %d, %Y · %I:%M %p UTC')

# Get the current time
current_time = datetime.now()

# Calculate the time 30 minutes ago
thirty_minutes_ago = current_time - timedelta(minutes=30)

while True:
    word = input("Enter a word in the format $xxxx or $xxx: ")
    if word.startswith('$') and len(word) in [4, 5]:
        print("Valid word format.")
        break
    else:
        print("Invalid format. Please enter the word again.")
print(word)
upper_word=word.upper()
print(upper_word)
# Filter tweets posted in the last 30 minutes containing the specified word
filtered_tweets = data[(data['date'] >= thirty_minutes_ago) & data['text'].str.contains(upper_word)]
print(filtered_tweets)

# Count occurrences of the specified word in the filtered tweets
count_of_word = filtered_tweets['text'].str.count(upper_word).sum()

print(f"Number of {word}: {count_of_word}")
