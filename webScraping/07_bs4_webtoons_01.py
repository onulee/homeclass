import requests
from bs4 import BeautifulSoup

url ="https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
# class 속성이 title 인 모든 "a" element 를 반환
for i,cartoon in enumerate(cartoons):  #index번호를 찍고 싶을때
    # print(i,":",cartoon.get_text())
    print("{} : {}".format(i+1,cartoon.get_text()))  
    
# for cartoon in cartoons:
#     print(cartoon.get_text())

