# 10. 결측치
# # 데이터 채우기 fillna
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# Nan 데이터를 빈 칸으로 채움
print(df.fillna(''))
print(df.fillna('없음'))

# 학교 데이터 전체를 Nan으로 채움
import numpy as np
df['학교'] = np.nan
print(df)

# Nan 으로 되어 있는 모든 칸을 모름으로 채움
# inplace=True 해야 반영됨.
df.fillna('모름',inplace=True)
# 반영하지 않으면 변경되지 않음.
print(df)


