#!/usr/bin/env python3
#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

r = requests.get('http://example.webscraping.com/')

html = r.content

html = html.decode('utf-8')

soup = BeautifulSoup(html,'html.parser')    #html.parser是解析器

code = soup.find_all('a')

for a in code:
    print(a.get_text())

# file_object = open('example.html', 'w')
# file_object.write(html.decode('utf-8'))
# file_object.close()