from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression, SGDClassifier 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split # train,test데이터분리
from sklearn.preprocessing import StandardScaler     # 정규화,표준화작업
from scipy.special import expit, softmax             # z점수 0-1사이의 값으로 변경
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, randint

# 데이터불러오기
wine = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
label = wine['class'].to_numpy()

# 데이터 분리-train_data,test_data
train_data, test_data, train_label, test_lebel = train_test_split(
    data, label, test_size=0.2, random_state=42)

# 알고리즘 선택
dt = DecisionTreeClassifier(random_state=42)

# # 검증세트를 2번 나누지 않음.
# # 교차검증 - 5파트로 나눠서 검증진행
# scores = cross_validate(dt, train_data, train_label)
# print(scores) # fit_time,score_time,test_score

# # # 교차검증 score 평균
# print(np.mean(scores['test_score']))  # 0.85530021470348

# # # StratifiedKFold()를 사용하여, 나누는 것을 상세하게 제어
# scores = cross_validate(dt, train_data, train_label, cv=StratifiedKFold())
# print(np.mean(scores['test_score']))

# n_splits 10개 폴드, shuffle 고르게 섞음
# splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
# scores = cross_validate(dt, train_data, train_label, cv=splitter)
# print(np.mean(scores['test_score']))

rgen = randint(0, 10)
print(rgen.rvs(10))

print(np.unique(rgen.rvs(1000), return_counts=True))
# params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}

# gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)

# gs.fit(train_data, train_label)

# dt = gs.best_estimator_
# print(dt.score(train_data, train_label))  #0.9615162593804117

# print(gs.best_params_)

# print(gs.cv_results_['mean_test_score'])









