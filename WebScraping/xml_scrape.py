# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:20:34 2017

@author: Yuna Noh
"""

import requests
from lxml import objectify

num_periods = "6"
div = "0"
state_id ="44"
num_months = "8"
year = "2016"

template_base= 'https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?parameter=tavg&'
template_add = template_base + 'state=%s&div=%s&month=%s&periods[]=%s&year=%s'
insert_these = (state_id, div, num_months, num_periods, year)
template_add = template_add %insert_these
response = requests.get(template_add).content
root = objectify.fromstring(response)

my_wm_username = "ynoh01"

print my_wm_username
print root["data"]["value"]
print root["data"]["twentiethCenturyMean"]
print root["data"]["lowRank"]
print root["data"]["highRank"]