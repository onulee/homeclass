# 10. 결측치
# # 데이터 삭제, dropna()
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# axis : index or columns
# index - row를 삭제, columns - 컬럼을 삭제
# how : any or all 
# any - Nan이 1개라도 있으면 삭제, all - 모두 있어야 삭제

# row에 Nan이 1개라도 있으면 삭제
# inplace=True 해야 반영됨.
print(df.dropna(axis='index', how='any'))
# print(df) 해보면 반영이 안되어 있음.

# SW특기 컬럼이 삭제
print(df.dropna(axis='columns'))

# 학교 컬럼 모두 Nan 입력
import numpy as np
df['학교'] = np.nan

# 컬럼이 모두 Nan일때 삭제 - 학교컬럼 삭제
print(df.dropna(axis='columns',how='all'))




