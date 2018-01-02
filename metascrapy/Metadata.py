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

        try:
            self.x_frame_options = result.headers['X-Frame-Options']
        except:
            pass

        soup = BeautifulSoup(result.content, "html.parser")

        funcs_title = [
            lambda x: x.find(property='og:title')['content'],
            lambda x: x.title.string
        ]
        self.title = self.parse(soup, funcs_title)

        soup_description = soup.find(property='og:description')
        if soup_description:
            self.description = soup_description['content']
        else:
            soup_first_paragraph = soup.find('p')
            if soup_first_paragraph:
                self.description = soup_first_paragraph.string
            else:
                self.description = None

        soup_image = soup.find(property='og:image')
        if soup_image:
            self.image = soup_image['content']
        else:
            self.image = None

        soup_paragraphs = soup.find_all("p",string=re.compile("\w+"))
        self.num_words = 0
        for sentence in soup_paragraphs:
            self.num_words += len(sentence.string.split())

        soup_html = soup.find('html')
        if soup_html:
            try:
                self.lang = soup_html['lang']
            except:
                self.lang = None
        else:
            self.lang = None