# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:43:22 2017

@author: Yuna Noh
"""
import requests
from bs4 import BeautifulSoup as bsoup
    
my_wm_username = 'ynoh01'

search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content

# Put your program here
parsed_html = bsoup(response, "lxml")
target_rows = parsed_html.find_all('tr')
    
my_result_list = []
for row in target_rows :
    county_row = []
    for x in row.find_all('td'):
        county_row.append(x.text.encode("ascii"))
        
    my_result_list.append(county_row)

print my_wm_username
print len(my_result_list)
print my_result_list


