# 함수사용해서 정규표현식 처리
import re
p = re.compile("ca.e")  #정해진 문자가 정규표현식에 맞는지 확인

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭 되지 않음")  

m = p.match("fecare care")    # match 는 주어진 처음부터 비교 careless 가능
                                         # care, careless,  caffe , good care, ... 테스트
print_match(m)
        
        
        

   
          
    
   
   





