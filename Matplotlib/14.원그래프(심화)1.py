import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd
import numpy as np

# df = pd.read_excel('score.xlsx')
# values = df.groupby('학교')
values = [30, 25, 20, 13, 10, 2]
colors = ['#ffadad','#ffd6a5','#fdffb6','#caffbf','#9bf6ff','#a0c4ff']
# colors = ['b','g','r','c','m','y']





# 축의 간격표시 이름
labels = ['Python','Java','Javascript','c#','c/c++','ETC']
explode = [0.05] * 6   

 
def custom_autopct(pct):
    # return ('%.1f%%' % pct) if pct >= 10 else ''
    # pct가 10보다 적으면 빈공백출력
    return '{:.1f}%'.format(pct) if pct >= 10 else ''

# wedgeprops 원그래프 도넛형태로 변경, 넓이가 0.6 남김, 0.8로 하면 0.8 남김
# edgecolor : 원영역별 테두리 추가
# linewidth : 원영역별 테두리 두께
wedgeprops = {'width':0.6, 'edgecolor':'w', 'linewidth':2}
plt.pie(values, labels=labels, autopct=custom_autopct, startangle=90, counterclock=False,colors=colors, \
    wedgeprops=wedgeprops, pctdistance=0.7)

plt.show()