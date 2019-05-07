import requests
from bs4 import BeautifulSoup
import json
from random import sample


class Parser:
    
    def __init__(self):
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}


    def parse(self, animal):
        """Choosing image & returning URL"""
        
        url = "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(animal)
        s = requests.Session()
        s.get('https://google.com', headers=self.HEADERS)
        req = s.get(url, headers=self.HEADERS).content
        soup = BeautifulSoup(req, "lxml")

        a = json.loads([i.text for i in sample(soup.find_all('div', {'class':'rg_meta'}), 1)][0])["ou"]
        
        return a

p = Parser()

