import requests
import json
from bs4 import BeautifulSoup

def pickle_task():
    url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    page=requests.get(url)
    # print(page)
    html=page.content
    # print(html)
    soup=BeautifulSoup(html,"html.parsar")
    # print(soup)
    div=soup.find("div",class_="_3RA-")
    # print(div)
    s=div.find()
    print(s)

pickle_task()  