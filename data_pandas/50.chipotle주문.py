import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.rcParams['font.family'] = 'Malgun Gothic' #windows
matplotlib.rcParams['font.size'] = 15  #글자크기 
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 글자 깨짐 해결 

# read_csv 함수로 데이터를 Dataframe 형태로 불러옵니다.
file_path = './chipotle.tsv'
df = pd.read_csv(file_path, sep = '\t')
print(df)
print(df.shape) # (4622, 5) 
print("------------------------------------")
print(df.info())

# 10개의 데이터 보여줌
df.head(10)

print(df.columns)
print("------------------------------------")
print(df.index)

df['order_id'] = df['order_id'].astype(str) # order_id는 숫자의 의미를 가지지 않기 때문에 str으로 변환.

print(df.describe()) # chipo dataframe에서 수치형 피처들의 요약 통계량을 확인.

print(len(df['order_id'].unique())) # order_id의 개수를 출력. 1834개 주문
print(len(df['item_name'].unique())) # item_name의 개수를 출력. 50개 목록(중복제외)

## 인사이트 발견 - 탐색과 시각화
# 가장 많이 주문한 item_name
# item_name당 주문량 확인

#### 가장 많이 주문한 item : top 10을 출력. [가장 많이 주문한 item]
item_count = df['item_name'].value_counts()[:10]
print(item_count)
# iteritems - 열을 계속으로 가져오기, iterrows() - 행을 계속적으로 가져오기
# for val, cnt in item_count.iteritems():
#     print("주문",":", val, cnt)
for idx, (val, cnt) in enumerate(item_count.iteritems()):
    print("주문", idx, ":", val, cnt)
    
### item당 주문 개수와 총량 구하기 
### item당 주문 개수   
order_count = df.groupby('item_name')['order_id'].count().sort_values(ascending=False)
order_count[:10] # item당 주문 개수를 출력합니다.    
print(order_count[:10])  

# print(df[['order_id','item_name','quantity']][0:100]) 

# item당 주문 총량을 출력
item_quantity = df.groupby('item_name')['quantity'].sum()
item_quantity[:10] # item당 주문 총량을 출력


item_name_list = item_quantity.index.tolist()
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()
 
plt.bar(x_pos, order_cnt, align='center')
plt.ylabel('주문량')
plt.title('주문량 그래프')
 
plt.show()