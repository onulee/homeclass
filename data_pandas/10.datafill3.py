# 10. 결측치
# # 데이터 삭제, dropna()
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# Nan가 포함되어 있는 row 전체를 삭제
# inplace=True 해야만 반영이 됨.
# print(df.dropna())
print(df.dropna(inplace=True))


