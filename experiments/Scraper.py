import urllib3
from bs4 import BeautifulSoup

quote_page = 'https://www.bloomberg.com/quote/SPX:IND'

page = urllib3.get_host(quote_page)

soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'companyName__99a4824b'})
name = name_box.text.strip()  # strip() is used to remove starting and trailing
print(name)
