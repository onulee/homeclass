# 12. 데이터 수정
# # column 수정
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)  

# 학교 컬럼중에 구로고를 영등포고로 변경
# print(df['학교'].replace({'구로고':'영등포고'}))
# 2개 이상일때
print(df['학교'].replace({'구로고':'영등포고','디지털고':'구청고'}))

# inplace=True 해야 반영이 됨.
df['학교'].replace({'구로고':'영등포고'},inplace=True) 
print(df)

# SW특기 컬럼 내용을 모두 소문자 변경
print(df['SW특기'].str.lower())
# SW특기 컬럼 - 대문자 변경
print(df['SW특기'].str.upper())
# 소문자 변경후 저장
df['SW특기'] = df['SW특기'].str.lower()
print(df)

# 고등학교를 입력하는 방법
df['학교'] = df['학교'] + '등학교'
print(df)
