import requests
import re
from bs4 import BeautifulSoup
import random


url = "https://www.digikala.com/search/category-mobile-phone/"

def download(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.findAll('img', src=re.compile('.jpg'))
    for info in links:
        link = info.get('src')
        with requests.get(link, stream=True)as r:
            name = random.randint(1, 100)
            with open(str(name)+ '.jpg', 'wb')as f:
                for pic in r.iter_content(chunk_size=1024):
                    f.write(pic)

download(url)                    