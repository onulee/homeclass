# 14. 그룹화
## 동일한 값을 가진 것들을 그룹으로 해서 통계,평균 등 값을 계산
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 학년 컬럼 추가
df['학년']=[3,3,2,1,1,3,2,2]
print(df)

# 학년별 그룹화 키합계 
print(df.groupby(['학교','학년']).sum())
# print(df.groupby('학년').sum().sort_values('키'))

# 학교로 그룹화를 한뒤 sw특기로 개수
# Nan을 제외한 개수 구로고3명, 디지털고 3명 
print(df.groupby('학교')['SW특기'].count())

# 학교로 그룹화해서 이름, sw특기로 개수 확인
print( df.groupby('학교')[['이름','SW특기']].count() )
