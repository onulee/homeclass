from numpy import column_stack
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# url 파일 불러오기
# urllib.request.urlretrieve : url에서 파일을 바로 다운로드
# urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt", filename="ratings.txt")
# train_data = pd.read_table('ratings.txt')

# 파일 저장하기
# train_data.to_csv('screen.csv',sep=',',encoding='utf-8-sig')

# 파일 불러오기
train_data = pd.read_csv('screen.csv')
print(train_data['document'])

# 총 개수 : 200000
# print(len(train_data))

# 100개로 test
train_data = train_data[:1000]

# Null 값이 존재하는 행 제거
# dropna(axis=0/1 index/columns, how='any'/'all')
train_data = train_data.dropna(how = 'any') 


# 정규 표현식을 통한 한글 외 문자 제거
# 문자열 일부만 치환하고 싶은 경우는 regex=True를 설정
train_data['document'] = train_data['document'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","", regex=True)

# 불용어 정의
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# 형태소 분석
okt = Okt()
tokenized_data = []
for sentence in train_data['document']:
    temp_X = okt.morphs(sentence, stem=True) # 형태소 어간으로추출
    temp_X = [word for word in temp_X if not word in stopwords] # 불용어 제거
    tokenized_data.append(temp_X)
    
# Word2Vec 훈련- 리스트에 리스트에 담김
from gensim.models import Word2Vec
model = Word2Vec(sentences = tokenized_data, vector_size = 100, window = 5, min_count = 5, workers = 4, sg = 0)

print(model.wv.most_similar("때"))

