# 1. series
# 1차원 데이터 (정수, 실수, 문자열 등)
import pandas as pd

# ## Series 객체 생성
# 예) 1월부터 4월까지 평균 온도 데이터 (-20, -10, 10, 20)
temp = pd.Series([-20, -10, 10, 20])
print(temp)

print(temp[0])  # 1월 온도
print(temp[2])  # 3월 온도