# 1. 그래프 기본
import matplotlib.pyplot as plt
# 한글 설정
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
# matplotlib.rcParams['font.family'] = 'AppleGothic' #Mac인 경우
matplotlib.rcParams['font.size'] = 15  #글자크기 

x=[1,2,3]
y=[2,4,8]

# x,y를 적용 - plt.bar(x,y) 막대그래프
plt.plot(x,y)
# plt.bar(x,y) # 막대그래프 그려짐
# 그래프 title설정, 한글은 설정을 해야 가능
plt.title('라인 그래프 Line Graph')
# 그래프를 보여줌.
plt.show()


