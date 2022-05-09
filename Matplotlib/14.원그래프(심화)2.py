import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd
import numpy as np
df = pd.read_excel('score.xlsx')
print(df['학교'].unique())
# 그래프 값
values = [df.groupby('학교').size()['구로고'],df.groupby('학교').size()['디지털고']]
# values = [df['학교'].value_counts()[0],df['학교'].value_counts()[1]]

# 학교 라벨 표시
labels=['구로고','디지털고']
# labels=[df['학교'].unique()[0],df['학교'].unique()[1]]
plt.pie(values,labels=labels)
plt.title('소속 학교')
plt.show()

print(values)