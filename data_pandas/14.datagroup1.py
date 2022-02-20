# 14. 그룹화
## 동일한 값을 가진 것들을 그룹으로 해서 통계,평균 등 값을 계산
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 그룹 설정
print(df.groupby('학교'))

# 그룹해서 구로고 정보 가져옴.
print( df.groupby('학교').get_group('구로고') )
# 그룹해서 디지털고 정보 가져옴.
# print( df.groupby('학교').get_group('디지털고'))

# 학교별 계산가능한 컬럼 평균 구함.
print(df.groupby('학교').mean())

# 그룹 학교별 크기(수)가 구해짐.
print(df.groupby('학교').size())

# 그룹 학교별 구로고 크기만 구해짐 - 5명
print(df.groupby('학교').size()['구로고'])

# 학교로 그룹화 후 키 평균을 구함.
print(df.groupby('학교')['키'].mean())

# 학교로 그룹화 하여 키, 국어, 영어, 수학 평균을 구함.
print(df.groupby('학교')[['키','국어','영어','수학']].mean())

# 학년추가