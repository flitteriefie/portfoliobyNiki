# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:30:54 2020

@author: sznik
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = 'https://www.ssga.com/uk/en_gb/intermediary/etfs/fund-finder'

main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle
driver.find_element_by_xpath(u'//a[text()="Professional Investor"]').click()
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to_default_content()

soup = BeautifulSoup (source, 'lxml')

#file = open('funds.txt', 'x')
file = open('Funds.txt', 'w')

#print(soup.prettify)
for fund in soup.find_all('td', class_='fundname'):
    print(fund)