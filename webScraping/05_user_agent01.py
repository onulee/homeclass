# 구글에서 user agent string
import requests
# url = "http://www.google.com"
url = "https://www.melon.com/chart/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()     #에러시 종료

with open("05_save01.html", "w", encoding="utf-8") as f:
    f.write(res.text)
    
    





