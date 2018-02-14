import bs4
import os
import requests

baseUrl = 'https://www.xkcd.com'
lastSeen = 1954 # I only want the recent stuff
count = 0
DEST = '/home/matt/AutomateBookLocal/xkcd'

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
url = 'https://xkcd.com{}'.format(prevLink.get('href'))
newNum = int(url[-5:-1]) + 1

# Download all comics since the most recent number
while newNum > lastSeen:
    url = '{}/{}'.format(baseUrl, lastSeen + 1)
    print('Downloading page {}...'.format(url))
    res, soup = getpage(url)
    
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'https:{}'.format(comicElem[0].get('src'))
            print('Downloading image {}...'.format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save the image to ./xkcd if it doesn't already exist
            if os.path.exists(os.path.join(DEST, os.path.basename(comicUrl))):
                print("{} already exists! Skipping it.".format(comicUrl))
            else:
                imageFile = open(os.path.join(DEST, os.path.basename(comicUrl)), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()
                print("Successful download!")
                count += 1
        except requests.exceptions.MissingSchema:
            print("There was a PROBLEM downloading at {}...".format(url))
    lastSeen += 1
print("\n{} new comics downloaded. Enjoy!".format(count))
