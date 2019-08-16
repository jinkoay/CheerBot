import requests
from bs4 import BeautifulSoup

'''
version 1
file contains image address in the same folder as this file
check for .jpeg and .gif file
'''
def run():
    url = 'http://attackofthecute.com/'
    page = requests.get(url).text
    
    soup = BeautifulSoup(page, 'lxml')
    
    imgs = set()
    
    for img in soup.findAll('img'):
        cur = img.get('src')
        idx = cur.find("http://cdn")
        endIdx = cur.find(".jpeg")
        if idx == -1: continue
        if endIdx != -1:
            imgs.add(cur[idx:(endIdx + 5)])
            continue
        endIdx = cur.find(".gif")
        if endIdx != -1:
            imgs.add(cur[idx:(endIdx + 4)])
            continue
    
    file = open("images.txt", "w")
    for img in imgs:
        file.write(img + "\n")
    
    file.close()
