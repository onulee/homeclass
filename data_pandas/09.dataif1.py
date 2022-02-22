# 9. 데이터 선택(조건)
# 조건에 해당하는 데이터 선택 
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 키가 185 이상인지 여부 True,False 출력 
print(df['키']>=185)

# 필터조건을 변수로 지정
filt = (df['키']>=185)
print(df[filt])  #필터 조건으로 출력
# print(df[df['키']>=185]) # 변수를 바로 적용
print(df[~filt]) # 필터 조전 반대로 출력

# 키가 185 이상인 학생들의 수학데이터 출력
# df.loc[row,column]
print(df.loc[df['키']>=185,'수학' ] )
print(df.loc[df['키']>=185,['이름','수학','과학'] ]) 