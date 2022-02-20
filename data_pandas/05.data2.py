# 5. 데이터 확인
# Series 확인
import pandas as pd

# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# series 에 대한 정보 출력
print(df['키'].describe())

# 키의 최소값
print("최소값 : ",df['키'].min())

# 키의 최대값
print(df['키'].max())

# 키 큰 순서대로 3명만 가져옴
print(df['키'].nlargest(3))

# 키의 평균
print(df['키'].mean())

# 키의 합
print(df['키'].sum())

# 개수count - 빈공백은 제외
print(df['SW특기'].count())

# 중복을 제거하고 학교이름 출력
print(df['학교'].unique())

# 중복을 제거하고 개수 출력
print(df['학교'].nunique())

