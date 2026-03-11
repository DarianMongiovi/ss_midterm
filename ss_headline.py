import requests
import random
import re

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

    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    chosen_category = random.choice(categories)
    
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'language': 'en',
        'apiKey': api_key,
        'category': chosen_category,
        'pageSize': 20
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get('status') == 'ok' and data.get('articles'):
            sample_articles = random.sample(data['articles'], k=min(5, len(data['articles'])))
            
            all_words = []
            for article in sample_articles:
                title = article.get('title', '')
                
                title = title.replace('-', ' ').replace('—', ' ')
                
                words = title.split()
                for w in words:
                    clean = w.strip(".,!?:;\"()[]{}*|#/@").lower()
                    
                    if clean.isalpha() and (len(clean) > 1 or clean in ['a', 'i']):
                        if w.isupper() and len(w) > 1:
                            continue
                            
                        all_words.append(clean)
            
            print(f"--- Topic: {chosen_category} | Words collected: {len(all_words)} ---")
            return all_words
        return []
    except Exception as e:
        print("Error:", e)
        return []

def word_list():
    return get_random_headline_words()
