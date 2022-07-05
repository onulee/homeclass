from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from scipy.special import expit
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd
from scipy.special import softmax

# 데이터 생성 - Species,Weight,Length,Diagonal,Height,Width
fish = pd.read_csv('https://bit.ly/fish_csv_data')
# print(fish.head())
# Species 중복제거 출력
print(pd.unique(fish['Species']))

# data = fish[['Weight','Length','Diagonal','Height','Width']]
# label = fish['Species']
# numpy변경
data = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
label = fish['Species'].to_numpy()

# train데이터, test데이터 분리
train_data,test_data,train_label,test_label = train_test_split(data,label,random_state=42)

# 데이터 전처리 스케일 조정, 정규화 작업
ss = StandardScaler()
ss.fit(train_data)
train_scaled = ss.transform(train_data)
test_scaled = ss.transform(test_data)

# 로지스틱 회귀 사용,  확률형태로 구분하기 쉽게 변경
lr = LogisticRegression(C=20)
lr.fit(train_scaled,train_label)
print(lr.predict(test_scaled[:5]))
print(lr.predict_proba(test_scaled[:5]))


score1 = lr.score(train_scaled,train_label)
print("정확도1 : ",score1)
score2 = lr.score(test_scaled,test_label)
print("정확도2 : ",score2)

# 기울기(가중치), Y절편
# print(lr.coef_,lr.intercept_)
# [[-0.4037798  -0.57620209 -0.66280298 -1.01290277 -0.73168947]] [-2.16155132]

decisions = lr.decision_function(train_scaled[:5])
print(np.round(decisions, decimals=2))

proba = softmax(decisions, axis=1)
print(np.round(proba, decimals=3))
