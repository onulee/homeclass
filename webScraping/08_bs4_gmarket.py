import requests
from bs4 import BeautifulSoup
import re

url="http://corners.gmarket.co.kr/Bestsellers"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# //*[@id="gBestWrap"]/div/div[3]/div[2]/ul/li[1]
bestlists = soup.find("div",{"id":"topPlusItems"}).find_next_sibling("div").find_all("li")
for i,blist in enumerate(bestlists):
    print("{}:{}".format(i+1,blist.find("a",{"class":"itemname"}).get_text()))


