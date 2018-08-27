'''
Author 	: Amila Silva
Email  	: amilacove@gmail.com
Date 	: 27/08/2018

This script crawls movie generes for the movie titles from IMDB
This script can be easily extended to crawl other information from IMDB
Input	: Movie Titles
Output 	: Genres
'''

from bs4 import BeautifulSoup
import re
import requests
import json

def extractGenre(movie_title):
	movie_search = '+'.join(movie_title.split())

	#extract the search page
	url = 'http://www.imdb.com/find?q=' + movie_search + '&s=tt&ref_=fn_tt'
	soup = BeautifulSoup(requests.get(url).text, 'lxml')

	#select the top search
	title_search = re.compile(r'/title/tt\d+/?ref_=fn_tt_tt_1')
	link = ''
	for item in soup.find_all(href = re.compile(r'/title/tt.*/?ref_=fn_tt_tt_1$')):
	    link = item['href']
	    break

	#extract genres for the movie
	if link != '':
	    urlPage = 'http://www.imdb.com' + link
	    soup = BeautifulSoup(requests.get(urlPage).text, 'lxml')

	    for item in soup.find_all(type="application/ld+json"):
	        jsonD = item.text
	        return json.loads(jsonD)['genre']

if __name__ == '__main__':
	movie = str(input('Movie Name: '))
	print(extractGenre(movie))
