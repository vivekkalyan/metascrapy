import sys
import requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
        print("Usage: scrape-meta-image.py <Link>")
else:
    result = requests.get(link)
    soup = BeautifulSoup(result.content, "html.parser")

    soup_title = soup.find(property='og:title')
    meta_title = soup_title['content']

    soup_description = soup.find(property='og:description')
    meta_description = soup_description['content']

    soup_image = soup.find(property='og:image')
    meta_image = soup_image['content']

    print(meta_title, meta_description, meta_image)