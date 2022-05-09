import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 

label = [ '강나래', '강태원', '강호림' ]  # 이름
values = [ 190,187,184 ]  # 키

# 막대그래프 그려짐, color='red' 약식 r
# plt.bar(label, values, color='r')

colors =['r','g','b'] # 컬러색 지정
# colors 3가지 색상을 적용, 투명도alpha
# plt.bar(label, values, color=colors, alpha=0.5)
# width bar의 두께 조절
plt.bar(label, values, color=colors, width=0.5, alpha=0.5)

# x축의 이름 45도 각도 조절
plt.xticks(label, rotation=45)  #글자가 길거나, 겹칠때 사용
plt.yticks(rotation=45)
# label 대신 ticks를 출력
ticks =['1번학생','2번학생','3번학생']
# plt.xticks(label, ticks, rotation=45) 

# y축 범위 제한 175-195
# plt.ylim(175,195)
# yticks 0부터 수치를 표시함. - 위부분에만 표시됨.
plt.yticks([0,175,180,185,190,195])

plt.show()