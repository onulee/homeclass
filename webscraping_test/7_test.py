import requests
from bs4 import BeautifulSoup

url = "https://www.goodchoice.kr/product/result?keyword=%EB%A6%AC%EC%A1%B0%ED%8A%B8"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("div",{"id":"poduct_list_area"}).find_all("li",{"class":"list_4 adcno2"})

for item in items:
    rate = item.find("p",{"class":"score"}).find("em").get_text()
    if float(rate)>=9.5:
        print(rate)
    else:
        continue    
    name = item.find("div",{"class":"name"}).find("strong").get_text()
    print(item.find("a")["href"])
    print(name)
