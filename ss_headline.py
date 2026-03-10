import requests
import random

def get_api_key():
    try:
        with open('api_key.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: api_key.txt not found!")
        return None

def get_random_headline_words():
    api_key = get_api_key()
    if not api_key: return []

    # List of categories to pick from randomly
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    chosen_category = random.choice(categories)
    
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'language': 'en',
        'apiKey': api_key,
        'category': chosen_category, # Randomize the topic
        'pageSize': 20               # Pull 20 options so we can shuffle them
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == 'ok' and data['articles']:
            # Pick 3 random articles from the 20 we fetched
            sample_articles = random.sample(data['articles'], k=min(3, len(data['articles'])))
            
            all_words = []
            for article in sample_articles:
                words = article['title'].split()
                clean_words = [w.strip(".,!?:;\"()").lower() for w in words]
                all_words.extend(clean_words)
            
            print(f"--- Topic chosen: {chosen_category} ---")
            return all_words
        return []
    except Exception as e:
        print("Error:", e)
        return []

word_list = get_random_headline_words()
