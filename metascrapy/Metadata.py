import requests
from bs4 import BeautifulSoup
import re
from functools import reduce

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
        self.lang = None

    def parse(self, content, funcs):
        for func in funcs:
            try:
                output = func(content)
                break
            except:
                pass
        else:
            output = None
        return output

    def scrape(self, link):
        self.__init_values()

        result = requests.get(link)
        soup = BeautifulSoup(result.content, "html.parser")

        funcs_xframeoptions = [
            lambda x: x.headers['X-Frame-Options']
        ]
        funcs_title = [
            lambda x: x.find(property='og:title')['content'],
            lambda x: x.title.string
        ]
        funcs_description = [
            lambda x: x.find(property='og.description')['content'],
            lambda x: x.find('p').string
        ]
        funcs_image = [
            lambda x: x.find(property='og:image')['content']
        ]
        funcs_numwords = [
            lambda x: reduce(lambda a,b: a+len(b.get_text().split()), x.find_all('p'), 0),
        ]
        funcs_lang = [
            lambda x: x.find('html')['lang']
        ]

        self.x_frame_options = self.parse(result, funcs_xframeoptions)
        self.title = self.parse(soup, funcs_title)
        self.description = self.parse(soup, funcs_description)
        self.image = self.parse(soup, funcs_image)
        self.num_words = self.parse(soup, funcs_numwords)
        self.lang = self.parse(soup, funcs_lang)