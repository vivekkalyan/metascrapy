import requests
from bs4 import BeautifulSoup

def meta_data(link):
    result = requests.get(link)
    soup = BeautifulSoup(result.content, "html.parser")

    soup_title = soup.find(property='og:title')
    if soup_title:
        meta_title = soup_title['content']
    else:
        meta_title = soup.title.string

    soup_description = soup.find(property='og:description')
    if soup_description:
        meta_description = soup_description['content']
    else:
        meta_description = soup.find('p').string

    soup_image = soup.find(property='og:image')
    if soup_image:
        meta_image = soup_image['content']
    else:
        meta_image = None

    return meta_title, meta_description, meta_image