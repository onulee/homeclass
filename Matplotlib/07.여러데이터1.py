import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
# 3개 데이터 표시
# 백신접종 인구
day = [ 1,2,3 ] # 1일, 2일, 3일
az = [ 2,4,8 ]   # ( 단위: 만명 ) 1일부터 3일까지 아스트라제네카 접종인구
pfizer = [ 5,1,3 ] # 화이자
moderna = [ 1,2,5 ] #모더나

plt.plot(day, az, label='az')
plt.plot(day,pfizer, label='pfizer',marker='o' , linestyle='--' )
plt.plot(day, moderna, label='moderna', marker='s', ls='-.' )
# lebel 표시
# plt.legend()
plt.legend(ncol=3) # lebel 옆으로 표시
plt.show()