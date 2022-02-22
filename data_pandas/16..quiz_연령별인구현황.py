import pandas as pd

# 남자데이터 출력
df = pd.read_excel('201202_201202_연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관',usecols='B,E:Y')
print(df.head(2))
# 1,195,951 -> 1195951 숫자로 변경(정수형으로 변경)
df.iloc[0] = df.iloc[0].str.replace(',','').astype(int)
# 전국데이터 출력
print(df.iloc[0])

# 여자데이터 출력
df_w = pd.read_excel('201202_201202_연령별인구현황_월간.xlsx',skiprows=3,index_col='행정기관',usecols='B,AB:AV')
print(df_w.head(2))

# 0~4세.1 .1이라는 것이 붙음. 2개가 있기에 붙여짐.
print(df.columns)
print(df_w.columns) # .1이라는것 붙음

df_w.columns = df.columns # 컬럼명을 남자의 것으로 통일
print(df_w.columns)

# 1,195,951 -> 1195951 숫자로 변경(정수형으로 변경)
df_w.iloc[0] = df_w.iloc[0].str.replace(',','').astype(int)
print(df_w)
