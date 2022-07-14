import requests
from bs4 import BeautifulSoup

# 크롤링할 사이트 주소 정의 
source_url = "https://namu.news/section/news?page="
table_rows = []

# 페이지를 넘겨가면서 a 태그 크롤링 수행, list 만들어주기 
for page in range(5):
    req = requests.get(source_url+str(page+1))
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    contents_table = soup.find(name="div", attrs={"class":"xmbqsi-8 gJSEHe"})
    table_rows.extend(contents_table.find_all(name="a"))

# a 태그의 href 속성을 리스트로 추출 
page_url_base = "https://namu.news"
page_urls = []
for row in table_rows:
    if len(row) > 0:
        page_url = page_url_base + row.get('href')
        page_urls.append(page_url)

# 중복 url 제거
page_urls = list(set(page_urls))

# 페이지 확인 
for page in page_urls:
    print(page)
    


#-----------------------------------------------------------
import pandas as pd
import re

# 제목과 본문을 받아올 dataframe 생성
columns = ['title', 'content_text']
df = pd.DataFrame(columns=columns)

# url에서 제목과 본문을 bs4를 이용해 스크래핑 해오기 
for page_url in page_urls:
    req = requests.get(page_url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    title = soup.find("div",{"class":"sc-1gwvzpi-1"})
    article = soup.find("article",{"class":"sc-1gwvzpi-20"})
    
    if title is not None:
        # separator : 내용들간 공백으로 분리, strip:앞뒤 공백제거
        row_title = title.get_text(separator=" ").strip()
    else:
        row_title = ""

    if article is not None:
        row_article = article.get_text(separator=" ").strip()
    else:
        row_article = ""
    
    row = [row_title, row_article]
    series = pd.Series(row, index=df.columns)
    # df = pd.concat([df,series],axis=0)
    print("-"*50)
    df = df.append(series, ignore_index=True)
    print(df)

# 텍스트에서 한국어만 정규식을 이용해 추출해냅니다. 
def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('',text)
    return result

df['title'] = df['title'].apply(lambda x: text_cleaning(x))
df['content_text'] = df['content_text'].apply(lambda x: text_cleaning(x))

# 제목과 본문이 잘 불러와졌는지 확인해봅니다.  
title_corpus = " ".join(df['title'].tolist())
content_corpus = " ".join(df['content_text'].tolist())
print(title_corpus)    

from konlpy.tag import Okt
from collections import Counter

nouns_tagger = Okt()
# 명사
nouns = nouns_tagger.nouns(content_corpus)
count = Counter(nouns)

# 편의를 위해 한 글자인 키워드 제거하기
remove_char_counter = Counter({x : count[x] for x in count if len(x) > 1})
print(remove_char_counter)
    
# 한국어 약식 불용어 사전을 이용해 키워드 가다듬기 (https://www.ranks.nl/stopwords/korean)
korean_stopwords_path = "deeplearning/korean_stopwords.txt"

with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]

# 문서의 특징에 따른 불용어를 추가하기 
namu_news_stopwords = ['연합뉴스', '저작권', '배포', '무단', '제공', '금지', '기자', '특파원', '사진', '시간', '지난해', \
    '지난', '이후', '관련', '자료', '오후', '이번', '내용', '영상', '대표', '지역', '혐의', '정부', '문제', '대해', '가장', '로이터', '보도']
for stopword in namu_news_stopwords:
    stopwords.append(stopword)

# 키워드 데이터에서 불용어를 제거하기 
remove_char_counter = Counter({x : remove_char_counter[x] for x in count if x not in stopwords})
print(remove_char_counter)    

# pip install pytagcloud pygame simplejson
# 3개를 설치해야 함.
import random
import pytagcloud
import webbrowser

# 상위 40개의 키워드를 추출합니다. 
ranked_tags = remove_char_counter.most_common(40)

# 추출한 키워드를 워드클라우드 이미지로 만들어 줍니다.  
# C:\Users\lee01\AppData\Local\Programs\Python\Python310\Lib\site-packages\pytagcloud\fonts

taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)
print(taglist)
pytagcloud.create_tag_image(taglist, 'wordcloud.jpg', size=(900, 600), fontname='NanumGothic', rectangular = False)
