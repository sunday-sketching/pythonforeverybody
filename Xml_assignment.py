import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

total = 0
url = input('Enter location: ') 
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
print('Count:', len(counts))
for c in tree.findall('.//comments/comment'):
    total = total + int(c.find('count').text)
print('Sum:', total)
