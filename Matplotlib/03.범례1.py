import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False  

x=[1,2,3]
y=[2,4,8]

# 범례추가
plt.plot(x,y, label='범례데이터' )
# 범례 표시 - 위치변경 loc
# plt.legend(loc='upper right')
# 구글  : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
# 범례 위치 x=0.5, y=0.5 기준은 0~1.0 사이
# plt.legend(loc=(0.5, 0.5))  
# plt.legend(loc=5)  # 숫자를 넣어도 됨. 구글 검색 참조
plt.legend(loc=(0.7, 0.8))  
plt.show()
