import bs4
import os
import requests
import sys

search_term = sys.argv[1] # "sankey" yields 4 results
LOCAL_DEST = '/home/matt/AutomateBookLocal/imgur'
BASE_URL = "https://imgur.com"
url = "{}/search/score?q={}".format(BASE_URL, search_term)

def get_page(dest):
    res = requests.get(dest)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "lxml")
    return res, soup

res, soup = get_page(url)

for link in soup.find_all('a'):
    link = link.get('href')
    # Request page if it's a search result
    if link.startswith('/gallery/'):
        img_res, img_soup = get_page("{}/{}".format(BASE_URL, link))
        # Find and download only post image(s)
        post_images = img_soup.find_all("div", {"class": "post-images"})
        for tag in post_images:
            img_tags = tag.find_all("img")
            for img in img_tags:
                print(img.get('src'))
                img_url = 'https:{}'.format(img.get('src'))
                img_res = requests.get(img_url)
                img_res.raise_for_status()               
                img_file = open(os.path.join(LOCAL_DEST, os.path.basename(img_url)), 'wb')
                for chunk in img_res.iter_content(100000):
                    img_file.write(chunk)
                img_file.close()
                print("Successful download!")
