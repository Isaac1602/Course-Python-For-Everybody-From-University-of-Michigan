import urllib.request
import json

url = input('Enter location: ')
data = urllib.request.urlopen(url)
info = json.loads(data.read().decode())

counts = []
comments = info.get('comments')
print('User count:', len(comments))

for item in comments:
    counts.append(int(item['count']))

print(sum(counts))