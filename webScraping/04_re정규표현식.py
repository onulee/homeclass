import re
# 정규표현식은 대입되는 문자를 비교해주는 식
# ca.e .은 1개의 자리에 문자가 들어가 있는지 확인해줌. 

p = re.compile("ca.e")  #정해진 문자가 정규표현식에 맞는지 확인
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de)  : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$)  : 문자열의 끝 > case, base (O) | face (X)

m = p.match("case")  # match 주어진 문장의 처음부터 case가 정규표현식 ca.e와 비교
# m = p.match("caffe") #에러
# print(m.group())       #맞으면 해당문자가 출력, caffe 매치되지 않으면 에러

if m:
    print(m.group())
else:
    print("매치 되지 않음")    






