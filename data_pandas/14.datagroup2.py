# 14. 그룹화
## 동일한 값을 가진 것들을 그룹으로 해서 통계,평균 등 값을 계산
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 학년 컬럼 추가
df['학년']=[3,3,2,1,1,3,2,2]
print(df)

# 학교,학년별 그룹화 평균구함
print(df.groupby(['학교','학년']).mean())

# 학년별 그룹화 평균구함.
print(df.groupby('학년').mean())

# 학년별 그룹화 키평균 순차정렬
print(df.groupby('학년').mean().sort_values('키'))

# 학년별 그룹화 키평균 역순정렬
print(df.groupby('학년').mean().sort_values('키',ascending=False))
