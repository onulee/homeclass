# 14. 그룹화
## 동일한 값을 가진 것들을 그룹으로 해서 통계,평균 등 값을 계산
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 학년 컬럼 추가
df['학년']=[3,3,2,1,1,3,2,2]
print(df)

# 학교로 그룹화 후 학년으로 학생수 확인
# df.groupby('학교')['학년'].value_counts() 2줄로 표현
school = df.groupby('학교')
print(school['학년'].value_counts())

# 학교로 그룹화 후 구로고 학생 학년으로 학생수 확인
# 구로고 1학년 2, 3학년-2명,2학년-1명
print(school['학년'].value_counts().loc['구로고'])
# print(school['학년'].value_counts().loc['디지털고'])

# 퍼센트로 확인(normalize=True)
print( school['학년'].value_counts(normalize=True).loc['구로고']  )