import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False  #마이너스 글자 깨짐 해결 
x=[1,2,3]
y=[2,4,8]

# 그래프 크기 조정, x로 10, y로 5
# plt.figure(figsize=(10,5))

# 그래프 크기 조정, x로 5, y로 10 
# plt.figure(figsize=(5,10))

# dpi : 해상도 확대 ( 50,70,100,200 )
plt.figure(figsize=(5,10),dpi=200)

# 배경색 - #efefef
plt.figure(facecolor='yellow')
# plt.figure(facecolor='#efefef')

# 그래프 내 grid 그려짐. axis='x' x축만, axis='y'는 y축만 그려짐.
plt.grid(axis='y', color='purple', alpha=0.2, linestyle='--', linewidth='2')
# plt.grid(axis='x')

plt.plot(x,y)

plt.show()