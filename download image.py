# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:43:54 2020

@author: sznik
"""



import requests

print('Beginning file download with requests')

url = ('https://wallpapersgood.com/resize/1400x1050/wallpapers/main/201645/akter-game-of-thrones-igra-prestolov-nicolaj-coster-waldau-nikolaj-koster-v.jpg')
r = requests.get(url)

with open('C:/Users/sznik/Desktop/hot.jpeg', 'wb') as f:
    f.write(r.content)

# Retrieve HTTP meta-data
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)