from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from scipy.special import softmax
from scipy.special import expit
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
import numpy as np
import pandas as pd

# 1. 데이터 가져오기
wine = pd.read_csv('https://bit.ly/wine_csv_data')
print(wine.head())
# print(wine['alcohol'].mean())
# print(wine.columns)
print(wine.info())     # null공백이 없는지 확인
print(wine.describe()) # 전반적인 정보확인

# 2. data, label분리
data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

# 3. train,test데이터 분리
train_data, test_data, train_label, test_label = train_test_split(
    data, target, test_size=0.2, random_state=42)

# 4. 정규화 작업
ss = StandardScaler()
ss.fit(train_data)
train_scaled = ss.transform(train_data)
test_scaled = ss.transform(test_data)

# SGDClassifier:분류모델일 경우 -> 반대 SGDRegressor:회귀모델일 경우
# SGDClassifier모델알고니즘이 아니라 방법에 속하기에 어떤 함수를 적용할지를 지정
# loss='log' 로지스틱 손실함수 적용
# 결과를 동일하게 하기 위해 random_state=42
# max_iter는 반복횟수
# SDGClassifier는 확률적 경사하강법만 가능, 배치,미니배치는 지원하지 않음

# sc = SGDClassifier(loss='log', random_state=42)
# train_score=[]
# test_score=[]
# # 300번 정도 반복을 해보고 그 가운데.... 반복횟수를 정함. fit메소드 사용후 partial_fit을 사용하면 class 필요없음.
# classes = np.unique(train_label)   # partial_fit메소드는 일부class만 사용하기에 class전부를 알려줌.
# for _ in range(0,300):   
#     # partial_fit 함수는 데이터의 일부만 전달될 수 있다고 가정하기에, 클래스(결과값)개수를 꼭 넘겨야 함.
#     sc.partial_fit(train_scaled,train_label,classes=classes)
#     train_score.append(sc.score(train_data,train_label))
#     test_score.append(sc.score(test_data,test_label))
# plt.figure(figsize=(8,6)) #그래프 가로세로크기설정
# plt.plot(train_score)
# plt.plot(test_score)
# plt.xlabel('epoch')
# plt.ylabel('accuracy')
# plt.show()


# sc = SGDClassifier(loss='log', max_iter=100, random_state=42)
# sc.fit(train_scaled,train_label) 
# print("정확도 : ",sc.score(train_scaled,train_label))
# print("정확도2 : ",sc.score(test_scaled,test_label))


# 1차적으로 로지스틱 함수를 사용해서 진행
# 5. 로지스틱 알고니즘 적용
# clists = [0.001,0.01,0.1,1,10,100]
# train_score = []
# test_score = []
# for clist in clists:
#     lr = LogisticRegression(C=clist)
#     lr.fit(train_scaled, train_label)
#     train_score.append(lr.score(train_scaled, train_label))
#     test_score.append(lr.score(test_scaled, test_label))
    
# plt.plot(np.log10(clists),train_score)
# plt.plot(np.log10(clists),test_score)
# plt.show()

lr = LogisticRegression(C=0.1)
lr.fit(train_scaled, train_label)

print(lr.score(train_scaled, train_label))
print(lr.score(test_scaled, test_label))

# # 기울기(가중치), Y절편
# print(lr.coef_, lr.intercept_)

# 5. 트리알고니즘 적용
# max_depth=3, depth를 3까지만 가능
# dt = DecisionTreeClassifier(random_state=42)
# dt.fit(train_scaled,train_label)

# # 그래프 그리기
# plt.figure(figsize=(10,7))
# plot_tree(dt,max_depth=1)
# # plot_tree(dt,max_depth=1, filled=True, feature_names=['alcohol','sugar','pH'])
# plt.show()

# # 특성 중요도 - 특성중에 어떤것이 가장 영향이 큰지를 알수 있음.
# print(dt.feature_importances_)

# print(dt.score(train_scaled,train_label))
# print(dt.score(test_scaled,test_label))