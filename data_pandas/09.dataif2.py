# 9. 데이터 선택(조건)
# 조건문 & and 그리고
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 키가 185보다 크고, 구로고에 다니는 학생 검색
print( df.loc[(df['키']>=185) & (df['학교']=='구로고')] )

# | or 또는 조건
# 키가 170보다 작거나, 200보다 큰 학생 검색
print( df.loc[(df['키']<170) | (df['키']>200 )] )
