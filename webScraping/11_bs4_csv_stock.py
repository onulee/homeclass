import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

#파일 저장
filename = "시가총액1-200.csv"
f=open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

# 상단 title 넣는 부분
title ="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))
writer.writerow(title)

for page in range(1,5):
    res = requests.get(url+str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    
    data_rows = soup.find("table",{"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns =row.find_all("td")
        if len(columns) <= 1:
            continue
        # data = [column.get_text().strip() for column in columns]
        data=[]
        for column in columns:
            # data = column.get_text().strip()
            data.append(column.get_text().strip())
           
            
        # print(data)
        writer.writerow(data)
        
    
    
    
    
    
    


