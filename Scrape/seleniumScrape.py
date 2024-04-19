from selenium import webdriver
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()

def scrape_twitter_account(account_url, word):
    # Open the URL in the browser
    driver.get(account_url)
    
    # Get the page source
    page_source = driver.page_source
    
    # Parse the page source using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')
    
    # Find spam in tweets in the HTML content using 'class': 'r-18u37iz'
    tweet_elements = soup.find_all('span', {'class': 'r-18u37iz'})
    # print(tweet_elements)
    for tweet_element in tweet_elements:
    # Find all links within the tweet elements
        tweet_links = tweet_element.find_all('a', {'class':'css-1qaijid r-bcqeeo r-qvutc0 r-poiln3 r-1loqt21'})
        print("A",tweet_links)
    word_count = 0
    
    # Regular expression to find the word in a tweet
    word_regex = re.compile(rf'\b{word}\b', re.IGNORECASE)
    
    # Loop through each tweet element
    for tweet_element in tweet_elements:
        tweet_text = tweet_element.text
        print("B",tweet_text)
        
        word_count += len(word_regex.findall(tweet_text))
    
    return word_count

# Function to scrape multiple Twitter accounts
def scrape_twitter_accounts(accounts, word):
        total_word_count = 0
        for account in accounts:
            word_count = scrape_twitter_account(account, word)
            total_word_count += word_count
        
        print(f"{word} was mentioned {total_word_count}")

accounts = [
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/warrior_0719',
    'https://twitter.com/ChartingProdigy',
    'https://twitter.com/allstarcharts',
    'https://twitter.com/yuriymatso',
    'https://twitter.com/TriggerTrades',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart'


]
word = '$TSLA'
scrape_twitter_accounts(accounts, word)

# Quit the WebDriver after use
driver.quit()
