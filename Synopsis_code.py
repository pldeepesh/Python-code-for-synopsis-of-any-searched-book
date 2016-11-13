# this gets the Synopsis for the searched book
import re
from bs4 import BeautifulSoup
import requests

_book_name = raw_input("enter the name of the book to get synopsis:")
_book_name_arr = []
_book_name_arr = _book_name.split()

#generating the Query URL

url = 'https://www.goodreads.com/search?q='

for i in _book_name_arr:
	url = url+i
	url = url+'+'
# print url[0:len(url)-1]
#getting the details from the generated url 
headers = {'User-agent': 'Mozilla/5.0'}
_html_code = requests.get(url,headers=headers)
# ,headers=headers)

#creating the soup
soup = BeautifulSoup(_html_code.text,"html.parser")
_link = soup.find('a',{'class':'bookTitle'})
_link = _link['href']

#getting the synopsis link for the searched book
_syn_link = 'http://www.goodreads.com'+_link

_syn_html = requests.get(_syn_link,headers=headers)

soup = BeautifulSoup(_syn_html.text,'html.parser')
break_down = soup.find('div',{'class':'readable stacked'})
print str(break_down.find_all('span')[1].contents)


