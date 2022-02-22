# 8. 데이터 선택(iloc)
# 위치를 이용하여 원하는 row에서 원하는 col선택
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)  
# 0번, 1번째 위치의 데이터 출력
# print(df.iloc[0])
# print(df.iloc[4])   # 4번, 5번째 학생 출력
print(df.iloc[0:5]) # row 0번부터 4번까지, 5번앞까지 출력 

# row 0번, 1컬럼 (0,1) - 1번째, 학교(1)가 출력
print(df.iloc[0,1])   # 구로고 출력
# 4번,2컬럼 (4,2) - 5번째,키 가 출력
print(df.iloc[4,2])  # 188 출력
print(df.iloc[[0,1],2])  # 0,1번 row 키 출력
print(df.iloc[[0,1],[3,4]])  # 0,1번 row 국어,영어 출력

# row 0-4번까지-5번앞까지, column 3-7번까지 출력
# 국어-사회까지
print(df.iloc[0:5,3:8])
print(df[0:5])  # row 슬라이싱
print( df[['이름','키']][:3] )