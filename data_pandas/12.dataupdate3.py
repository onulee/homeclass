# 12. 데이터 수정
# # column 삭제
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)  

#column추가
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
print(df)

# 총합 column 삭제, inplace=True해야 반영
df.drop(columns=['총합'],inplace=True)
print(df)

# 국어,영어,수학 column 삭제
df.drop(columns=['국어','영어','수학'],inplace=True) 
print(df)
