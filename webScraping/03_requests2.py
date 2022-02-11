import requests
res = requests.get("http://www.google.com")
#res = requests.get("http://www.naver.com")
#res = requests.get("http://www.daum.net")
res.raise_for_status()     #에러시 종료

print(res.text)         # 내용을 모두 출력
print(len(res.text))    # 글자수를 알수 있음. 

with open("01_save01.html", "w", encoding="utf-8") as f:   # 파일 쓰기 모드
    f.write(res.text)                                                     # 파일 저장

# 구글로도 진행
# 다음으로 진행


