#! /usr/bin/python3
# chap11PracProjImageSiteDownloader.py

import bs4
import os
import requests
import sys

searchTerm = sys.argv[1]
baseUrl = 'https://imgur.com'
searchUrl = baseUrl + '/search/score?q=' + searchTerm

def getpage(destination):
    res = requests.get(destination)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    return res, soup

res, soup = getpage(searchUrl)

# Loop through all links
for link in soup.find_all('a'):
    linkHere = link.get('href')
    # Request page if link starts with '/gallery/' (is a search result)
    if linkHere[0:9] == '/gallery/':
        print(linkHere)
        res2, soup2 = getpage(baseUrl + linkHere)
        # Find and download only post image(s)
        divPostImages = soup2.find_all("div", {"class": "post-images"})
        for tag in divPostImages:
            imgTags = tag.find_all("img")
            for img in imgTags:
                print(img.get('src'))
                imgUrl = 'https:' + img.get('src')
                imgRes = requests.get(imgUrl)
                imgRes.raise_for_status()
                
                imgFile = open(os.path.join('imgur', os.path.basename(imgUrl)), 'wb')
                for chunk in imgRes.iter_content(100000):
                    imgFile.write(chunk)
                imgFile.close()
                print("Successful download!")
