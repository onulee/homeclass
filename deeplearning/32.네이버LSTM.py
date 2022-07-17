import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request
from konlpy.tag import Okt
from tqdm import tqdm
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#----------------------------------------------------------------
# https://wikidocs.net/44249

# 1. 파일 불러오기 - 단어는 500개까지만 출력
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt", filename="ratings_train.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt", filename="ratings_test.txt")

train_data = pd.read_table('ratings_train.txt')
test_data = pd.read_table('ratings_test.txt')

# 1-2. 훈련용 리뷰 개수 출력
# 훈련용 리뷰 개수 : 150000
print('훈련용 리뷰 개수 :',len(train_data)) 
# print(train_data[:5]) # 상위 5개 출력
# print('테스트용 리뷰 개수 :',len(test_data)) # 테스트용 리뷰 개수 출력

# 1-3. 중복제거
# document 열과 label 열의 중복을 제외한 값의 개수
# (146182, 2)
train_data['document'].nunique(), train_data['label'].nunique()

# document 열의 중복 제거
train_data.drop_duplicates(subset=['document'], inplace=True)

# 총 샘플 개수
print('총 샘플의 수 :',len(train_data))

# 그래프 그리기
train_data['label'].value_counts().plot(kind = 'bar')
plt.show()

# 긍정,부정 개수 확인
#    label  count
# 0      0  73342
# 1      1  72841
print(train_data.groupby('label').size().reset_index(name = 'count'))




