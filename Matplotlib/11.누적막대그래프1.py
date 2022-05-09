import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd

df = pd.read_excel('C:\pyFolder\js_work\score.xlsx')

# 누적막대그래프 그리기, bottom 아래부터 순서정함.
# 국어 주석처리하고 보면 수학점수가 떠 있음 
plt.bar(df['이름'],df['국어'], label='국어' )
plt.bar(df['이름'],df['영어'], bottom=df['국어'],label='영어')
plt.bar(df['이름'],df['수학'], bottom=df['국어'] + df['영어'], label='수학')


plt.xticks(rotation=60)
plt.legend()

plt.show()