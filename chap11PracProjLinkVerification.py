#! usr/bin/python3
# chap11PracProjLinkVerification.py

import bs4
import requests

url = 'https://www.unbundledfares.com/'
broken = []
skipped = []

def getpage(destination):
    res = requests.get(destination)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    return res, soup

# Download page
res, soup = getpage(url)

# Find and loop through all links on page
for link in soup.find_all('a'):
    print(link.get('href'))
    linkHere = link.get('href')

    # Try to visit page and download content
    if linkHere[0:4] == 'http':
        r = requests.get(linkHere)
        report = r.status_code
        if report == 404:
            print("Oops, 404 here!")
            broken.append(linkHere)
        else:
            print(report)
    # Skip if it's not an 'http' address
    else:
        print("Skipped: " + linkHere)
        skipped.append(linkHere)
    
# Print broken list
print("There are " + str(len(broken)) + " broken links.")
for link in broken:
    print(link)

# Print skipped list
print("There are " + str(len(skipped)) + " skipped links.")
for link in skipped:
    print(link)
