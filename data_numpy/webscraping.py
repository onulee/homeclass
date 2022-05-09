import requests
from bs4 import BeautifulSoup
headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36" }

url="https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
content = soup.find("div",{"class","viewtype catal_ty"})
print(content)

# with open("google_movie.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
# print(soup.prettify())