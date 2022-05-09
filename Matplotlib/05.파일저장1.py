from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False  #마이너스 글자 깨짐 해결  
x=[1,2,3]
y=[2,4,8]

plt.plot(x,y)

# 파일저장 - png로 저장
# plt.savefig('graph.png')
plt.savefig('graph.png',dpi=100)

# dpi 200크기로 출력
plt.figure(dpi=200)
plt.plot(x,y)
plt.show()
plt.savefig('graph_200.png',dpi=300)

# plt.show()