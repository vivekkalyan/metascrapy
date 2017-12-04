import requests
from bs4 import BeautifulSoup
import re
import functools

class Metadata(object):
    """docstring for Metadata"""
    def __init__(self):
        super(Metadata, self).__init__()

    def __init_values(self):
        self.title = None
        self.description = None
        self.image = None
        self.x_frame_options = None
        self.num_words = None

    def scrape(self, link):
        self.__init_values()
        result = requests.get(link)

        try:
            self.x_frame_options = result.headers['X-Frame-Options']
        except:
            pass

        soup = BeautifulSoup(result.content, "html.parser")
        soup_title = soup.find(property='og:title')
        if soup_title:
            self.title = soup_title['content']
        else:
            self.title = soup.title.string

        soup_description = soup.find(property='og:description')
        if soup_description:
            self.description = soup_description['content']
        else:
            self.description = soup.find('p').string

        soup_image = soup.find(property='og:image')
        if soup_image:
            self.image = soup_image['content']
        else:
            self.image = None

        soup_paragraphs = soup.find_all("p",string=re.compile("\w+"))
        self.num_words = 0
        for sentence in soup_paragraphs:
            self.num_words += len(sentence.string.split())
