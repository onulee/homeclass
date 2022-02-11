import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=703846&weekday=tue"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td",{"class":"title"})
# print(cartoons)
## 1개 가져오기
# title = print(cartoons[0].a.get_text())     #글자 1개를 가져옴.
# link = print("https://comic.naver.com"+cartoons[0].a["href"]) #링크정보 가져오기

## 링크 구하기
for i,cartoon in  enumerate(cartoons) :
    title = cartoons[i].a.get_text()     #글자 여러개를 가져옴.
    link = "https://comic.naver.com"+cartoons[i].a["href"] #링크정보 가져오기
    print(title,":",link)
    
total_rates=0    
cartoons = soup.find_all("div",{"class":"rating_type"})
for i,cartoon in enumerate(cartoons):
    rate = cartoon.find("strong").get_text()
    total_rates += float(rate)  # 소수점까지 표현
    print(rate)  
    
print("전체 점수 : ", round(total_rates,2))   #소수점 제한
print("평균 점수 : ", total_rates / len(cartoons))    #cartoons 개수   