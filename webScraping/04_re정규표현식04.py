# 함수사용해서 정규표현식 처리
import re
p = re.compile("ca.e")  #정규표현식 형태 지정

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")  

m = p.search("good care") #주어진 문자열 중에 일치 하는지 비교
print_match(m)
lst = p.findall("careless good care cafe")  #list 형태로 반환
print(lst)
        
        
        

   
          
    
   
   





