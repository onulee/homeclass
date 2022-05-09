import pandas as pd
import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 

df = pd.read_excel('score.xlsx',index_col='지원번호')

# label = [ '강나래', '강태원', '강호림' ]  # 이름
# values = [ 190,187,184 ]  # 키
# colors =['r','g','b'] # 컬러색 지정

label = df['이름']
values = df['키']
colors =['r','g','b'] # 컬러색 지정

# bar뒤 h만 붙이면 옆으로 막대그래프 그려짐
# plt.barh(label, values, color=colors)
# # y축에서 ->축바뀜,  x축 범위 제한 175-195
# plt.xlim(175,195)

plt.ylim(165,210)
bar = plt.bar(label, values, color=colors)
# 막대그래프 무늬 채움. matplotlib hatch
bar[0].set_hatch('/')  # 막대그래프 무늬 / 채워짐
bar[1].set_hatch('x')  # 무늬 x채워짐
bar[2].set_hatch('..')  # 무늬 ..채워짐

#  rect bar의 정보를 받아옴, 막대그래프 위 values[190,187,184]값 표시
for idx,rect in enumerate(bar):
    # bar의 정보가 1개씩 대입, get_height 글자 위치 위쪽으로 0.5만큼 이동
    plt.text(idx,rect.get_height()+0.5,values[idx],ha='center',color='blue')
    # plt.text(idx,values[idx]+0.5,values[idx],ha='center',color='blue')

plt.show()