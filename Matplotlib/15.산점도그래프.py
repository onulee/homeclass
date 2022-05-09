import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd
import numpy as np
import re

df = pd.read_excel('score.xlsx')
df['학년'] =[3,3,2,1,1,3,2,2]

# numpy random 배열 8개 생성 : 0.0 ~ 1.0사이의 랜덤수 생성
# 크기를 키우기 위해 * 1000
# sizes = np.random.rand(8)*1000
# print(sizes)

# 학년별 크기 설정
# 1학년 500, 2학년 1000, 3학년 1500
sizes = df['학년'] * 500 

# 산점도 그래프 : scatter, 산점도 크기 설정 s
# c : color , cmap : 컬러맵  구글검색 : matplotlib cmap 
# alpha 투명도
plt.figure(figsize=(10,10))
plt.scatter(df['영어'],df['수학'],s=sizes, c=df['학년'], cmap='viridis',alpha=0.5 )
plt.xlabel('영어')
plt.ylabel('수학')
# 컬러바 생성, ticks: 바눈금, shrink 사이즈조절, orientation 위치 가로방향
plt.colorbar(ticks=[1,2,3],label='학년',shrink=0.5,orientation='horizontal') 
plt.show()