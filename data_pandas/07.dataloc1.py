# 7. 데이터 선택(loc)
# 이름을 이용하여 원하는 row에서 원하는 col선택
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

print(df.index)  # index 전체출력
print(df['이름']) # 이름컬럼 전체 출력
# index 1번에 해당하는 전체 row데이터
# print(df.loc['1번'])
# print(df.loc['5번'])

# index 1번 학생, 국어컬럼만 가져옴
print(df.loc['1번','국어'])  # 90나타남.

print(df.loc[['1번','3번'],'영어']) #1번,3번 학생 영어성적 컬럼만
print(df.loc[['1번','3번'],['영어','수학']]) #1번,3번 학생 영어,수학 성적 컬럼만
print(df.loc[['1번','3번']]) #1번,3번 전체 컬럼 출력

# 1번~5번까지 학생, 국어~사회성적까지 출력
# 보통 : 하면 앞전까지 인데... 여기는 5번 포함 됨
print(df.loc['1번':'5번','국어':'사회'])

