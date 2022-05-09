import enum
from re import L
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 
import pandas as pd
import numpy as np

# 데이터 값 - 100비율을 맞춤. 
# labels와 크기 맞춤.
values = [30, 25, 20, 13, 10, 2]
# values = [1,1,1,1,1,1]      # 비율을 균등하게 해도 됨.
# 축의 간격표시 이름
labels = ['Python','Java','Javascript','c#','c/c++','ETC']

# 원형을 띄우기
explode = [0.1,0,0,0,0,0]   # 처음 1개만 띄움
# explode = [0.2,0.1,0,0,0,0] # 2개만 띄움
# explode = [0.05] * 6 # 전체를 0.05간격만큼 띄움

#원형 그래프 출력, 간격표시는 labels사용
# autopct 그래프 안 수치표시, %% 2번 넣으면 %단위 출력
# startangle시작지점을 90도에서 시작
# counterclock 시계방향으로 데이터 출력
plt.pie(values, labels=labels, explode=explode, autopct='%.1f%%', startangle=90, counterclock=False)

plt.title('언어별 선호도')
#범례
plt.legend(loc=(1.2,0.3),title='언어별 선호도')
plt.show()