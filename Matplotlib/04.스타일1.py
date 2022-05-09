import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False  #마이너스 글자 깨짐 해결 

# marker 마커 스타일
x=[1,2,3]
y=[2,4,8]

# linewidth 라인 두께를 줌
# plt.plot(x,y,linewidth=2)

# 지점에 'o'표시, 라인은 숨김
# plt.plot(x,y,marker='o',linestyle='None')

# 지점에 v표시, 삼각표시,사이즈를 10 키움.
# plt.plot(x,y,marker='v',markersize=10)
# 지점에 X표시
# plt.plot(x,y,marker='X', markersize=10)
# markeredgecolor는 marker테두리표시, markerfacecolor 색채움
# plt.plot(x,y,marker='X', markersize=10,markeredgecolor='red',markerfacecolor='yellow')

# 라인스타일을 정함.
plt.plot(x,y,linestyle=':')
plt.show()