import pandas as pd

# 상단 2개 제외, 처음1개는 컬럼으로 지정되어서, 2개만 가져오면 됨.
# index.name이 없으면 번호로 넣으면 됨. 0
df = pd.read_excel('score.xlsx')
print(df.sort_values('키'))