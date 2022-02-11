import re

p = re.compile("ca.e")
# m = p.match("caffe")
# print(m.group())

def print_match(m):
    if m:
        print("m.group() :",m.group())
        print("string :",m.string)
        print("m.start() :",m.start())
        print("m.end() :",m.end())
        print("m.span() :",m.span())
    else:
        print("매칭된 것이 없음.") 
        
m = p.match("cafe")
# m = p.search("good care")
print_match(m)

lst = p.findall("good care cafe case")
print(lst)
print(lst[1])
       
