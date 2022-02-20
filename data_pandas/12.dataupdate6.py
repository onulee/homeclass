# 12. 데이터 수정
## column 순서변경
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)  

#column추가
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
# print(df)

# 결과 column을 추가하고 전체 데이터는 Fail 초기화
df['결과'] ='Fail' 
# print(df)

# 총합이 400보다 큰 데이터에 대해서 합격
df.loc[df['총합'] > 400,'결과'] = 'Pass'
print(df) 

#column순서 변경
cols = list(df.columns)
print(cols)

# 맨뒤 결과 column을 앞쪽으로 변경, 나머지 column 순차적으로 출력
# cols[-1] -> list여야 해서, [ ]안에 추가적으로 넣음.
df = df[[cols[-1]]+cols[0:-1]]
# df = df[['결과','이름','학교']]   #결과, 이름, 학교 출력 됨.
print(df)

