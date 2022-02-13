import re
import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

items = soup.find_all("li",{"class":re.compile("^search-product")})
# print(items[0].find("div",{"class":"name"}).get_text())

for idx,item in enumerate(items):
    # 광고 상품 제외
    if "search-product__ad-badge" in item["class"]:
        # print(item["class"])
        print("광고상품 제외")
        continue
    name = item.find("div",{"class":"name"}).get_text()
    # Apple 상품 제외
    if "Apple" in name:
        print(" >>>>> Apple 상품 제외")
        continue
    
    # 평점비교
    rate = item.find("em",{"class":"rating"})  # get_text() 에러남.
    if rate:
        rate = rate.get_text()
    else:
        print("평점 없는 상품 제외")  
        continue  
    
    
    #리뷰 수 비교
    rate_cnt = item.find("span",{"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()  #글자출력 (45)
        rate_cnt = rate_cnt[1:-1]        #앞,뒤1 만큼 제외
        # 리뷰수 100개 밑으로 제외
        if int(rate_cnt) < 100:
            print("리뷰수 100개 밑으로 제외")
            continue
    else:
        print("리뷰 개수 없는 상품 제외")    
    
    
    if float(rate) >=5.0 and int(rate_cnt) > 100 :
        price = item.find("strong", {"class":"price-value"}).get_text() # 가격
        print("평점 : {}, 리뷰수 : {}, 가격 : {}".format(rate,rate_cnt,price))
        print(name)
    else:   
        continue
    
        
print("총개수 : ",len(items))
