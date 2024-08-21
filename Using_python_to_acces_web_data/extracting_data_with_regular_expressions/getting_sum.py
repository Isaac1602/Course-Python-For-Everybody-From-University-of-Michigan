import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
"""
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
"""

#url = 'http://py4e-data.dr-chuck.net/comments_2066154.html'
#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
file = urllib.request.urlopen(input('Dame la URL: '))
#file = urllib.request.urlopen(url).read()
soup = BeautifulSoup(file, 'html.parser')

spans = soup('span')

numbers = []
for span in spans:
    number = span.string
    numbers.append(int(number))

print(sum(numbers))

#https://github.com/richyvk/python-web-data help from