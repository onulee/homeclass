import pandas as pd

# 상단 2개 제외, 처음1개는 컬럼으로 지정되어서, 2개만 가져오면 됨.
# index.name이 없으면 번호로 넣으면 됨. 0
df = pd.read_excel('stat_142801.xls',skiprows=2,nrows=2,index_col=0)
print(df)

# 출생아 수 0번째 row를 출력하려면 에러가 남.
# print(df.loc[0])  
# index 출력 ( 출생아 수 -> 출생아\xa0수 되어 있음)
print(df.index) # index 잘 나오지만  df.index.values 출력하면 다름
# index list형태로 모두 출력
print(df.index.values)
# ['출생아\xa0수' '합계\xa0출산율'] # 유니코드 띄워쓰기가 들어감

# index name변경을 해줌.
df.rename(index={'출생아\xa0수':'출생아 수','합계\xa0출산율':'합계 출산율'},inplace=True)
print(df.loc['출생아 수'])

df = df.T # row,column축 변경
print(df) 



