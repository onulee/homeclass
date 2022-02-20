# 9. 데이터 선택(조건)
# str함수
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 이름이 송으로 시작하는 학생 검색
filt = df['이름'].str.startswith('김')
print(df[filt])

# 이름이 근이 들어가는 학생 검색
filt = df['이름'].str.contains('근')
print(df[filt])
print(df[~filt]) # 근이 들어가는 학생 제외 학생출력

# 특기가 python,java 인 학생 검색 - ## -> 대소문자 구분을 함.
# PYTHON 대문자 검색이 안됨.
langs = ['python','java']
filt = df['SW특기'].isin(langs) 
print(df[filt])

# 검색할 문자를 모두 소문자로 변경 lower()
langs = ['python','java']
filt = df['SW특기'].str.lower().isin(langs) 
print(df[filt])

# sw특기 중 Nan이 있으면 error가 남.
filt = df['SW특기'].str.contains('Java')
# print(df[filt])

#----------------------------

# isin(langs) 검색시 Nan은 False로 검색이 됨
# contains 검색시 Nan은 Nan 검색이 되어 조건 실패됨.
print(df['SW특기'].str.lower().isin(langs)) # Nan->False
## Nan -> Nan 출력 
print(df['SW특기'].str.contains('Java')) 
## Nan -> True,False 출력
print(df['SW특기'].str.contains('Java',na=True))
print(df['SW특기'].str.contains('Java',na=False))

# Java가 들어가는 SW특기 검색
filt = df['SW특기'].str.contains('Java', na=False)
print(df[filt])



