# 4. 파일저장 및 열기
# 엑셀(.xlsx)파일 열기
import pandas as pd

data1 = pd.read_csv('2014년졸음운전교통사고.csv',encoding='euc-kr') 
data2 = pd.read_csv('2015년졸음운전교통사고.csv',encoding='euc-kr') 
data3 = pd.read_csv('2016년졸음운전교통사고.csv',encoding='euc-kr') 

df = pd.concat([data1,data2,data3])
df.set_index('구분',inplace=True)
print(df)






