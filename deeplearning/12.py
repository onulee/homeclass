from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from scipy.special import expit
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.special import softmax

df = pd.read_csv('deeplearning/iris(150).csv')
print(df['Species'].unique()) # 중복된 row1개만 출력

data = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# df['Species'] = df['Species'].apply(nameChange)  # 함수호출, 변경값:df 적용
label = df['Species']

data_numpy = np.array(data) 
label_numpy = np.array(label) 

# # train데이터, test데이터 분리
train_data,test_data,train_label,test_label = train_test_split(data_numpy,label_numpy,random_state=42)

# 데이터 전처리 스케일 조정, 정규화 작업
ss = StandardScaler()
ss.fit(train_data,train_label)
train_scaled = ss.transform(train_data)
test_scaled = ss.transform(test_data)

# 로지스틱 회귀 사용,  확률형태로 구분하기 쉽게 변경
lr = LogisticRegression(C=5)
lr.fit(train_scaled,train_label)
print(lr.predict(test_scaled[:5]))
print("-"*50)
print(lr.predict_proba(test_scaled[:5]))

score1 = lr.score(train_scaled,train_label)
print("정확도1 : ",score1)
score2 = lr.score(test_scaled,test_label)
print("정확도2 : ",score2)

decision = lr.decision_function(test_scaled[:5])
print(np.round(decision,decimals=2))

proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))

 