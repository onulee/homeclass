# 5. 데이터 확인
# DataFrame 확인
import pandas as pd

# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# 숫자컬럼인 경우 column별로 개수, 평균, 표준편차, 최소값, 최대값
# 각 지점별 평균, 평균을 보완할 목적으로 사용
# print(df.describe())
print(df['키'].describe())  # 컬럼별 describe

# 컬럼별 타입
# print(df.info()) 

# 처음 5개의 row 데이터를 가져옴.
# print(df.head())
# print(df.head(7))  #처음7개 row 데이터를 가져옴.
# print(df.tail())  # 마지막 5개 row 데이터를 가져옴
# print(df.tail(3))   # 마지막 3개 row 데이터를 가져옴.
# print(df.values)  # 배열구조로 출력
print(df.index)
print(df.index.values) # index list로 보여짐. 

# print(df.index)   # index 출력
# print(df.columns)   # 상단의 컬럼 출력
print(df.shape)   # row,column수를 보여줌





