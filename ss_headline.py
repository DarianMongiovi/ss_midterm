import requests

API_KEY = 'YOUR_ACTUAL_API_KEY'

def get_headline_words():
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'language': 'en',
        'apiKey': API_KEY,
        'pageSize': 3  # We only want 3 headlines
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == 'ok':
            all_words = []
            
            for article in data['articles']:
                headline = article['title']
                # Split the headline into a list of words
                words = headline.split()
                # Clean up punctuation and add to our master list
                clean_words = [w.strip(".,!?:;\"()").lower() for w in words]
                all_words.extend(clean_words)
            
            return all_words
        else:
            print("API Error:", data.get('message'))
            return []

    except Exception as e:
        print("Connection Error:", e)
        return []

if __name__ == "__main__":
    word_list = get_headline_words()
    
    print(f"--- Captured {len(word_list)} total words ---")
    print(word_list)