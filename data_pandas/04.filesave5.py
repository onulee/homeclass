# 4. 파일저장 및 열기
# 엑셀(.xlsx)파일 열기
import pandas as pd

# 엑셀파일 열기
df = pd.read_excel('score.xlsx')
# print(df)

# index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)





