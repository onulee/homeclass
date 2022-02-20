# 12. 데이터 수정
## row 삭제
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)  

#column추가
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
print(df)

# 4번 index, row 삭제, inplace=True해야 반영됨.
# df.drop(index='4번',inplace=True)
# print(df)

# 수학점수가 80점 미만 학생만 남기고, 삭제
# 1번=100,6번=95,8번=90 이상인 학생 삭제
filt = df['수학'] < 80
# print(df[filt])

# 80점 밑으로 삭제시
# index를 출력하면 80점 밑으로 index가 출력됨.
print(df[filt].index)
# 이 index번호를 drop에 넣어주면 됨.
print(df.drop(index=df[filt].index))
# inplace=True 해야 반영됨.
print(df)