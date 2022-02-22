# 6. 데이터 선택(기본)
# Column 선택(label) - 슬라이싱
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# 영어컬럼에서 0~4까지 가져옴. 5번 앞까지
print(df)
print(df['이름'])
print( df['영어'][0:5] )

# 이름,키 컬럼에서 0-2까지, 3번째 앞까지 가져옴.
print( df[['이름','키']][:3] )

# 3번 앞까지 전체 컬럼을 가져옴.
print(df[:3])

# [1:] 2번부터, [2:] 3번 다음 이후 다 가져옴
# print(df[0:])  #1번째 컬럼부터 
# print(df[3:])  #4번째 컬럼부터
print(df.iloc[[0,1,3]])  #row 0,1,3 부분으로 가져올때 사용


