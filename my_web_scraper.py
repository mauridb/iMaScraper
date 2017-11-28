from bs4 import BeautifulSoup

import requests
import datetime
import os
import sys
import logging

logging.basicConfig(filename="scrape.log", level=logging.DEBUG)


def get_data(url):
	response = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
	# print dir(response)
	return response.text


html_doc = get_data(sys.argv[1])
soup = BeautifulSoup(html_doc, 'html.parser')

print dir(soup)
print "\n********\n*********\n"
# print soup.prettify()
print soup.find_all('a')
