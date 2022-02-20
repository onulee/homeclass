# 12. 데이터 수정
## row 추가, cell수정
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)  

#column추가
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
print(df)

# 결과 column을 추가하고 전체 데이터는 Fail 초기화
df['결과'] ='Fail' 
# print(df)

# 총합이 400보다 큰 데이터에 대해서 합격
df.loc[df['총합'] > 400,'결과'] = 'Pass'
# print(df)

# 새로운 row추가
df.loc['9번'] = ['유승찬','단지고',184,90,90,90,90,90,'Django',(90*5),'Pass']
print(df)

# cell 수정 - 4번학생, SW특기 수정
df.loc['4번','SW특기'] = 'Python'
print(df)

# cell 5번 학생의 학교-디지털고, SW특기-C 수정
df.loc['5번',['학교','SW특기']] = ['디지털고','C']
print(df)