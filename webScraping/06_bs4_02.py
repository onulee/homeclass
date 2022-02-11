import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 a element 를 찾아줘
print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upload" 인 어떤 element 를 찾아줘

print(soup.find("li", attrs={"class":"rank01"}))
# rank = soup.find("li",{"class":"rank01"})    #attrs 생략가능
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling)
rank2 = rank1.next_sibling.next_sibling   # 줄바꿈도 다음으로 인식함. 그래서 2번해야 함.
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())                       # 글자를 찍을때 get_text()
rank2 = rank3.previous_sibling.previous_sibling  #이전 태그로 이동
print(rank2.a.get_text())                                 
print(rank1.parent)    #부모로 이동
rank2 = rank1.find_next_sibling("li")   #개행문자,줄바꿈 제외하고 다음 li 첫번째를 찾음
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())
rank2 = rank3.find_previous_sibling("li")  #개행문자,줄바꿈 제외하고 이전 li 첫번째를 찾음
print(rank2.a.get_text())

print(rank1.find_next_siblings("li"))  #li 복수로 가져옴.

webtoon = soup.find("a", text="독립일기-11화 밥공기 딜레마") #a 태그의 text 내용으로 찾음.
print(webtoon)    
    





