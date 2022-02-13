import requests
res = requests.get("http://google.com") 
#res = requests.get("http://www.jolse.com/category/moisturizer/1017/?page=2")
print("응답코드 :", res.status_code) # 200 이면 정상
res.raise_for_status()   # 에러시 프로그램 종료
if res.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")
# print(len(res.text))
# print(res.text)

with open("mygoogle2.html", "w", encoding="utf-8") as f:
    f.write(res.text)

