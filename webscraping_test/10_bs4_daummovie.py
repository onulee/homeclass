import requests
from bs4 import BeautifulSoup

for year in range(2018,2022):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img",{"class":"thumb_img"})
    for idx,image in enumerate(images):
        image_url = image["src"]
        
        if idx==5:
            break
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
                f.write(image_res.content)