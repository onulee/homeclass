import requests
from bs4 import BeautifulSoup
import re

# page 값을 활용해서 검색
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
url="http://corners.gmarket.co.kr/Bestsellers"
res = requests.get(url,headers=headers)
print("응답코드 : ",res.status_code)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
div_products = soup.find("div",{"id":"gBestWrap"})
id_products = div_products.find("div",{"id":"topPlusItems"}).find_next_sibling("div")
products = id_products.ul.find_all("li")
print("ro : ",len(products))
for idx,product in enumerate(products):
    name = product.find("a",{"class":"itemname"}).get_text()
    if name:
        print("{} : {}".format(idx+1,name))
    else:
        print("없음")    
        continue


