from numpy import column_stack
import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# 영화리뷰 감성분류 - CNN사용
# https://wonhwa.tistory.com/35
#트레인 파일 불러오기 - delimiter:분리표시, quoting : 3개까지 묶기 
train_data = pd.read_csv('deeplearning/ratings_train.txt',header = 0, delimiter = '\t', quoting=3)
print('학습데이터 전체 개수: {}'.format(len(train_data)))

#리뷰 전체길이 확인
train_length = train_data['document'].astype(str).apply(len)
print(train_length.head())

#리뷰 통계 정보
print('리뷰 길이 최댓값: {}'.format(np.max(train_length)))
print('리뷰 길이 최솟값: {}'.format(np.min(train_length)))
print('리뷰 길이 평균값: {:.2f}'.format(np.mean(train_length)))
print('리뷰 길이 표준편차: {:.2f}'.format(np.std(train_length)))
print('리뷰 길이 중간값: {}'.format(np.median(train_length)))
print('리뷰 길이 제1사분위: {}'.format(np.percentile(train_length,25)))
print('리뷰 길이 제3사분위: {}'.format(np.percentile(train_length,75)))