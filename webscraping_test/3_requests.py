# pip install requests       # 웹 정보 요청하는 라이브러리
# pip install beautifulsoup4 # HTML 및 XML 파일에서 원하는 데이터를 손쉽게 Parsing 
# pip install lxml           # css 문법으로 특정 요소를 쉽게 가져옴
import requests
from bs4 import BeautifulSoup
url="https://comic.naver.com/index"
headers = {"User-Agent":"https://www.whatismybrowser.com/detect/what-is-my-user-agent"}
res = requests.get(url,headers = headers)
print(">> 여기서 부터 응답코드 : ",res.status_code)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text, "lxml")
data_rank = soup.find({"ol":"asideBoxRank"})
cartoons = data_rank.find_all("li")
for i in range(0,10): 
    print(i,",",cartoons[i].a.get_text())  
    
## 정규표현식
## 랭킹가져오기
## 이미지 다운로드
## 주식정보 가져오기
## 쿠팡 판매순위, 별점, 후기등록 체크 검색
## 네이버 자동로그인

