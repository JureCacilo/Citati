from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://quotes.yourdictionary.com/theme/marriage/"

response = urlopen(url).read()
soup = BeautifulSoup(response, "lxml")

i = 0
for quote in soup.findAll("p", attrs={"class": "quoteContent"}):
    i+= 1

    print(str(i) + " quote: " + quote.string)

    if i == 5:
        break
