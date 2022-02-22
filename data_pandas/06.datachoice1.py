# 6. 데이터 선택(기본)
# Column 선택(label) - 정수index로 가져오기
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# 컬럼으로 가져올때 컬럼을 입력 : df['키'], df['이름']...
# print(df['키'])
# 이름,키 2개를 가져올때 
# print(df[['이름','키']])

print(df.columns[0])

# 컬럼 확인 - 정수 index로 가져올때
print(df.columns)
print(df.columns[0]) # 0번째 이름 컬럼확인
print(df['이름'])
# print(df.columns[2]) # 2번재 키 컬럼확인

# # 컬럼 : [이름] 가져옴.
# print(df[df.columns[0]]) # df['이름'] 와 같음.
# # print(df['이름'])

# # 마지막 컬럼을 가져올때
# # 데이터의 컬럼수가 너무 많을때 제일 뒤 선택방법
print(df[df.columns[-1]])
# 여러개 가져올때 [[ ]] 2개사용
print(df[df.columns[[0,3,-1]]])


