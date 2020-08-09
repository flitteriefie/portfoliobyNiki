# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:25:58 2020

@author: sznik
"""

from bs4 import BeautifulSoup
import requests

def define(unknown):
    source = requests.get(('https://www.thefreedictionary.com/'+ unknown)).text
    soup = BeautifulSoup (source, 'lxml')
    for ds in soup.find_all('div', class_='ds-list'):
        #print(ds.prettify)
        exact = ds.text
        print(exact)
    

define('unbuoyed')

