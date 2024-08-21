import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

page = urllib.request.urlopen(input("Enter URL: "))
soup = BeautifulSoup(page, "html.parser")

spans = soup('span')

numbers = []

for span in spans:
    numbers.append(int(span.string))

print (sum(numbers))