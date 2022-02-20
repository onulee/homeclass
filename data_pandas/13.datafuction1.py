# 13. 함수적용
## 컴럼 내용 변경
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 학교 글자에 문자를 추가하는 것은 가능 ( 문자형데이터 + 문자형데이터 )
# 숫자에 글자를 추가하는 것은 불가능 - 함수를 적용해서 처리
df['학교'] = df['학교']+'등학교'
print(df)

# 키에 cm을 추가하려면 에러 (예: 197cm) 
# 키 정수형데이터 + 문자형데이터 = error
# df['키'] = df['키']+'cm'
# print(df)

# 정수형데이터 + 정수형데이터 가능
df['키'] = df['키']+ 100
print(df)