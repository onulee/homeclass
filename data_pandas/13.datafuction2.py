# 13. 함수적용
## 컴럼 내용 변경
import pandas as pd
# 엑셀파일 index지정해서 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)  

# 키 뒤에 cm을 추가하는 함수
def add_cm(height):
    return str(height)+'cm'

# 키 데이터를 add_cm함수를 호출해서 적용후 리턴
df['키'] = df['키'].apply(add_cm)
print(df)

# SW특기 첫글자 대문자 뒤 소문자로 변경
def capchange(lang):
    if pd.notnull(lang): # Nan인지 확인
        return lang.capitalize() #첫글자 대문자, 나머지 소문자
    return lang

# capchange함수적용
# df['SW특기'] = df['SW특기'].apply(capchange)
# print(df)

# 함수 적용하지 않아도 첫글자 대문자, 나머지 소문자적용
# print(df['SW특기'].str.capitalize())
df['SW특기'] = df['SW특기'].str.capitalize()
print(df)
        
        

