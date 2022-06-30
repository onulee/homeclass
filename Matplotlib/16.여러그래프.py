import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd
import numpy as np
import re
 
df = pd.read_excel('score.xlsx')
# 가로2개, 세로2개의 크기 생성 figsize 그래프 크기 키움.
fig, axs = plt.subplots(2,2,figsize=(15,10))
fig.suptitle('4개 그래프') #4개 전체 그래프제목

# 4개 그래프 : 1번째 axs[0,0],2번째 axs[0,1], axs[1,0], axs[1,1]
# 1번째 그래프 생성
axs[0,0].bar(df['이름'],df['국어'],label='국어') # 바그래프
axs[0,0].set_title('첫번째 그래프') # 제목
axs[0,0].legend() 
axs[0,0].set(xlabel='이름',ylabel='점수') # x,y축 label
axs[0,0].set_facecolor('lightyellow') # 배경색
axs[0,0].grid(linestyle='-',linewidth=0.5)

# 2번째 그래프
axs[0,1].plot(df['이름'],df['수학'],label='수학')
axs[0,1].plot(df['이름'],df['영어'],label='영어')
axs[0,1].legend()

# 3번째 그래프
axs[1,0].barh(df['이름'],df['키'])

# 4번째 그래프
axs[1,1].plot(df['이름'],df['사회'],color='g',alpha=0.5)


plt.show()


