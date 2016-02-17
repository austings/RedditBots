import urllib.request
from bs4 import BeautifulSoup
import sys
import time

link = 'http://www.thefreedictionary.com/socialism'
url = ("https://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=define+socialism&userip=24.93.24.159")
headers= {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
req= urllib.request.Request(url, None, {'Referer': "none"})

while True:
	print("Trying to connect to online dictionary...")
	try:
		with urllib.request.urlopen(req) as response:
		   page = response.read()
		print("Data pulled!")
		break
	except urllib.error.HTTPError as e:
	    print("503 Error: Search is currently unavailable.")
	    time.sleep(5)
	

page = str(page)
page = page[(page.find('Merriam-Webster","content":"'))+28:(page.find("},{")-1)]
saveFile = open('lastDefinition.txt','w')
saveFile.write(page)

saveFile.close()

print("Complete")