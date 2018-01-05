#! /usr/bin/python3
# chap15PracProjComicDownloader.py

import bs4
import os
import requests

baseUrl = 'https://www.xkcd.com'
lastSeen = 1933
count = 0

def getpage(destination):
    res = requests.get(destination)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    return res, soup

# Get number of most recent comic's permanent number
# Navigate to previous from home page, then add one to url permanent number 
# because home page doesn't have permanent number in url.
print('Launching xkcd...')
res, soup = getpage(baseUrl)
prevLink = soup.select('a[rel="prev"]')[0]
url = 'https://xkcd.com' + prevLink.get('href')
newNum = int(url[-5:-1]) + 1

# Download all comics since the most recent number
while newNum > lastSeen:
    url = baseUrl + '/' + str(lastSeen + 1)
    print('Downloading page ' + url + '...')
    res, soup = getpage(url)
    
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save the image to ./xkcd if it doesn't already exist
            imgName = os.path.basename
            if os.path.exists(os.path.join('xkcd', os.path.basename(comicUrl))):
                print(comicUrl + " already exists! Skipping it.")
            else:
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
                print("Successful download!")
                count += 1
        except requests.exceptions.MissingSchema:
            print("There was a PROBLEM downloading at " + url + "...")
    lastSeen += 1
print("\n" + str(count) + " new comics downloaded. Enjoy!")
