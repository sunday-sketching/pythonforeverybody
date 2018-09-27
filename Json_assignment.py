import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
url_open = urllib.request.urlopen(url)
data = url_open.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

total = 0
count = 0
for comment in info["comments"]:
    total += comment["count"]
    count += 1
print("Count: ", count)
print("Sum: ", total)
