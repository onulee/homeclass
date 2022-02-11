# beautifulsoup4가 설치되어 있어야 함.
# pip install beautifulsoup4    # 웹스크래핑때 사용
# pip install lxml                  # 구문 파싱할때 사용
import requests
from bs4 import BeautifulSoup
# 네이버 웹툰 검색
url = "https://comic.naver.com/webtoon/weekday"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()     #에러시 종료

soup = BeautifulSoup(res.text,"lxml") #text을 lxml파싱해서 soup담음.
print(soup)                 #전체페이지 html코드 출력
print("title : ",soup.title) #title태그가 출력.
print("title : ",soup.title.get_text())   #title태그 안 글자출력.
print("a : ", soup.a)    #soup의 제일 처음 a태그가 출력
print("a속성 : ",soup.a.attrs)  #a태그의 속성 값들이 dictionary로 출력
print("a속성 1개 : ", soup.a["href"]) #a태그의 href속성정보 출력



    
    





