import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find("ol",{"id":"realTimeRankFavorite"}).find_all("li")
# class 속성이 title 인 모든 "a" element 를 반환
for i,cartoon in enumerate(cartoons):  #index번호를 찍고 싶을때
    print("{} : {}".format(i+1,cartoon.get_text()))  
    


