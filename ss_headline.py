import requests

def get_api_key():
    try:
        # 'r' means read mode
        with open('api_key.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: api_key.txt not found!")
        return None

def get_headline_words():
    api_key = get_api_key()
    if not api_key:
        return []

    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'language': 'en',
        'apiKey': api_key,
        'pageSize': 3 
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data['status'] == 'ok':
            all_words = []
            for article in data['articles']:
                # Using .split() to turn the headline string into a list of words
                words = article['title'].split()
                # Clean up punctuation and lowercase everything
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
    print(f"Total words found: {len(word_list)}")
    print(word_list)
