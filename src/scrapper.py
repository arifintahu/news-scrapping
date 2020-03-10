# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:15:39 2020

@author: miftahul.arifin
"""

import requests
from bs4 import BeautifulSoup

class Scrapper():
	"""docstring for Scrapper"""
	def __init__(self, url):
		r = requests.get(url)
		self.soup = BeautifulSoup(r.content, 'html5lib')

	def getTitle(self):
		news = []
		article = self.soup.findAll('article')
		for i in article:
			title = i.find(attrs = { 'class' : 'title'})
			if(title != None):
				news.append(title.text)
		return news

	def getHeadline(self):
		headline = self.soup.find('div', attrs = { 'id' : 'headline' })
		title = headline.find(attrs = { 'class' : 'title' })
		return title.text

scrap1 = Scrapper("https://www.cnnindonesia.com/nasional")
article = scrap1.getTitle()
headline = scrap1.getHeadline()
print(headline)
		