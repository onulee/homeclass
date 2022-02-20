# 10. 결측치
# # 데이터 채우기 fillna
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# SW특기 데이터 중에서 Nan에 대해서 채움
# 반영하려면 inplace=True
df['SW특기'].fillna('확인 중',inplace=True)
print(df)

