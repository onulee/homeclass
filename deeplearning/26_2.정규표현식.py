import re

##### 해당문구에서 한글만 추출하시오. #####
##### 함수를 사용하시오. #####

book = '좋은 하루 맞나요?^^V ㅎㅎ  정말 good!! 이 집!! 짱임**##@^^ '

def text_cleaning(text):
    # 한글의 정규표현식으로 한글만 추출.
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub('', text)
    return result



result = text_cleaning(book)

print(book)
print(result)