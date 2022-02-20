# 1. series
# 1차원 데이터 (정수, 실수, 문자열 등)

import pandas as pd

# ## Series 객체 생성
temp = pd.Series([-20,-10,10,20], index=['Jan','Feb','Mar','Apr'])
print(temp)

print(temp['Jan'])       # Index Jan (1월) 에 해당하는 데이터 출력
print(temp['Apr'])       # Index Apr (4월) 에 해당하는 데이터 출력

# temp['Jun'] # 존재하지 않는 Index 접근 시도 시 에러
