import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False #마이너스 글자 깨짐 해결 
x=[1,2,3]
y=[2,4,8]

# marker 표시
plt.plot(x,y,marker='o')

# 반복적으로 좌표에 값을 표시
# for idx,txt in enumerate(y):
#     # x[0],x[1],x[2] y[0],y[1],y[2] 좌표
#     # y좌표에서 0.3추가이동 , ha 수평정렬-가운데, 글자색-블루
#     plt.text(x[idx], y[idx]+0.3, txt, ha='center',color='blue')

plt.text(x[0], y[0]+0.3, y[0], ha='center',color='blue')
plt.show()