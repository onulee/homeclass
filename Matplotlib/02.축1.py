import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False  

x=[1,2,3]
y=[2,4,8]
plt.plot(x,y)
# X선 설명, 색상 들어감,위치 : left, center,right
plt.xlabel('X축',color='red',loc='right')
 # Y선 설명, 생상 들어감, 위치 : top,center,bottom
plt.ylabel('Y축',color='#00aa00',loc='top') 
# 그래프 x,y표시 간격
plt.xticks([1,2,3])
plt.yticks([3,6,9,12])

# 개별 폰트 설정 가능
plt.title('꺾은선 그래프', fontdict={'family':'HYGungSo-Bold','size':20}) 
plt.show()

