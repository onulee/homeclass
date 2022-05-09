import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd
import numpy as np

df = pd.read_excel('C:\pyFolder\js_work\score.xlsx')

#numpy
# print(np.arange(5))  # [0,1,2,3,4] 5개array배열을 생성
# print(np.arange(3,6)) # [3,4,5] 3개array배열을 생성
# arr = np.arange(5) 
# print(arr)  # [0,1,2,3,4] 배열생성
# print(arr+100) # 각배열요소에 100더해짐
# print(arr * 3)   # 각배열요소에 3이 곱해짐

# df 가로,세로 구조출력
# print(df.shape)  # (8,10) x,y 좌표크기 출력
# print(df.shape[0])  # 8 x좌표 크기 출력

N = df.shape[0]  # 8 x좌표 크기
index = np.arange(N)  #8개배열구조 생성[0,1,2,3,4,5,6,7]

# 전체 화면 크기 확대 - 전체화면을 그리고 bar그래프를 그려야 함.
plt.figure(figsize=(10,5))
plt.title('학생별 성적')

# index-w : 중앙지점에서 -0.25왼쪽에서 막대그래프 생성
# width=w : 두께를 0.25로 주면 막대그래프가 겹치지 않고 나옴.
w=0.25
plt.bar(index-w,df['국어'], width=w, label='국어')
plt.bar(index,df['영어'], width=w, label='영어' )
plt.bar(index+w,df['수학'], width=w, label='수학')

plt.grid(axis='y',alpha=0.2)
# label출력시 입력 ncol=3 옆으로 길게 나옴.
plt.legend(ncol=3)
# x 축 index값출력을 이름으로 변경
plt.xticks(index,df['이름'],rotation=60)

plt.show()