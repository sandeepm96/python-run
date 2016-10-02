from bs4 import BeautifulSoup
from urllib import FancyURLopener
import codecs

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

mopen = MyOpener()
doc = mopen.open('http://lecturenotes.in').read()
soup = BeautifulSoup(doc)
pretty = soup.prettify().encode("utf-8")

with open("index.html", 'w') as wws:
    wws.write(pretty)
