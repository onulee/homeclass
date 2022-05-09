import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False  #마이너스 글자 깨짐 해결 

# marker 마커 스타일
x=[1,2,3]
y=[2,4,8]

# linestyle 라인스타일을 정함. 점선모양
# plt.plot(x,y,linestyle=':')
# 줄선모양
# plt.plot(x,y,linestyle='--')
# 줄선. 점 모양
# plt.plot(x,y,linestyle='-.', color='pink')

#선 색상 - #ff0000
# plt.plot(x,y,linestyle='-.', color='g')  #color='b'

# plt.plot(x,y,'ro--')  # r-red color, o-둥근marker, -- 점선 linestyle 의미
# plt.plot(x,y,'bv:')      # b-blue color, v-삼각marker, : 둥근점선 의미       
plt.plot(x,y,'go')
plt.plot(x,y, color='g',marker='o', linestyle='none')
# 선색상 투명도 지정
plt.plot(x,y,alpha=0.3) 

plt.show()