# 11. 데이터 정렬
# # sort_values 오름차순, 내림차순
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 키를 기준으로 오름차순(낮은키 부터) 정렬
print(df.sort_values('키'))

# 키를 기준으로 내림차순 정렬
print(df.sort_values('키',ascending=False))

# 수학,영어를 기준으로 내림차순 정렬
# 3번, 4번 수학 70, 영어 75,60 로 정렬됨.
print(df.sort_values(['수학','영어'],ascending=False ))
# 수학, 영어 점수 기준으로 오름차순 정렬
# 3번, 4번 70, 영어 60,75로 정렬 됨.
print( df.sort_values(['수학','영어']))
# print( df.sort_values(['수학','영어'],ascending=False))

# 수학 오름차순, 영어-내림차순 정렬
print(df.sort_values(['수학','영어'],ascending=[True,False]) )

# series 1차원도 가능 - 키 기준으로 오름차순 정렬
print(df['키'].sort_values() )

# 키 기준 내림차순 정렬
print(df['키'].sort_values(ascending=False) )

# 지원번호 기준 오름차순
print( df.sort_index() )

# 지원번호 기준으로 내림차순
print( df.sort_index(ascending=False)  )

