from sklearn.model_selection import cross_validate
from sklearn.linear_model import LogisticRegression, SGDClassifier 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split # train,test데이터분리
from sklearn.preprocessing import StandardScaler     # 정규화,표준화작업
from scipy.special import expit, softmax             # z점수 0-1사이의 값으로 변경
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터불러오기
wine = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
label = wine['class'].to_numpy()

# 데이터 분리-train_data,test_data
train_data, test_data, train_label, test_lebel = train_test_split(
    data, label, test_size=0.2, random_state=42)

# 데이터분리 - sub_data,val_data
sub_data, val_data, sub_label, val_label = train_test_split(
    train_data, train_label, test_size=0.2, random_state=42)

print(sub_data.shape, sub_label.shape)

# 알고리즈 선택
dt = DecisionTreeClassifier(random_state=42)
# 훈련
dt.fit(sub_data, sub_label)
#정확도
print(dt.score(sub_data, sub_label))
print(dt.score(val_data, val_label))


