import pandas as pd

data = {
    '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
    '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data)
# print(df)

import random
df['요일'] = 1
for i in range(8):
    df.loc[i,'요일'] = random.randint(1,6)

def change(x):
    if x == 0 :
        return '월'
    elif x == 1 :
        return '화'
    elif x == 2 :
        return '수'
    elif x == 3 :
        return '목'
    elif x == 4 :
        return '금'
    elif x == 5 :
        return '토'
    else :
        return '일'

df['요일'] = df['요일'].apply(change)

print(df)
print(df['요일'])
# print(df.iloc[0][4])


# df['요일'] = random.randint(1,6)
# print(df)
