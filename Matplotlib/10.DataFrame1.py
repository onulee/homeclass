import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd

df = pd.read_excel('C:\pyFolder\js_work\score.xlsx')
# 가로 : 지원번호 , 세로 : 키
# plt.plot(df['지원번호'],df['키'])

# 가로 : 지원번호, 세로 : 영어 2개의 그래프를 동시에 출력
plt.plot(df['지원번호'],df['영어'])
plt.plot(df['지원번호'],df['수학'])

# plt.ylim(0,350)

# 그래프 내 grid 그려짐. axis='x' x축만, axis='y'는 y축만 그려짐.
plt.grid(axis='y', color='purple', alpha=0.2, linestyle='--', linewidth=2)
# plt.grid(axis='x')

plt.show()