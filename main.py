import requests
import time
from bs4 import BeautifulSoup
import telegram

# Your telegram token and chat_id
token = '6058033545:AAHdlKgiyqPOR-JAESst6Wruj4o5j62IDeY'  # Your Telegram Bot token
bot = telegram.Bot(token='6058033545:AAHdlKgiyqPOR-JAESst6Wruj4o5j62IDeY')
chat_id = '717335888'  # Your chat id

# Login to the website once
session = requests.Session()
login_url = 'https://www.tesmanian.com/account/login'
username = 'pashadzyba1997@gmail.com'  # you need to use your username and password to login
password = 'qwerty54321'
login_data = {
    'email': username,
    'password': password
}
session.post(login_url, data=login_data)
articles_data = []
while True:
    try:
        url = 'https://www.tesmanian.com/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        req = requests.get(url, headers=headers)

        soup = BeautifulSoup(req.text, 'html.parser')
        articles = soup.find_all('blog-post-card', class_='blog-post-card')
        # Find all the articles
        for article in articles:
            if article is None:
                continue
            url = "https://www.tesmanian.com/" + article.find('a', class_="blog-post-card__figure").get('href')
            title = article.find('img', class_='w-full h-full object-cover zoom-image').get('alt')
            articles_data.append({
                "title": title,
                "url": url
            })


    except Exception as e:
        print(f'Error: {e}')
    for telegram_msg in articles_data:
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + str(
            telegram_msg)
        print(url_req)
        results = requests.get(url_req)
        print(results.json())
        time.sleep(15)
