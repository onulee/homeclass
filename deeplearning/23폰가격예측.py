from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold, cross_validate, train_test_split # train,test
from sklearn.preprocessing import PolynomialFeatures, StandardScaler     # 정규화,표준화작업
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from statsmodels.stats.outliers_influence import variance_inflation_factor
import seaborn as sns
import warnings
# warnings.filterwarnings("ignore")

file_path = 'deeplearning/used_mobile_phone.csv'
# file_path = 'C:\pyFolder\js_work\deeplearning\used_mobile_phone.csv'
df = pd.read_csv(file_path)
print(df.info())

# price_index : 이동통신 물가지수 월별존재
print(df.head())

# create_date로부터 ‘월’을 의미하는 month 정보를 피처로 추출합니다.
# 2017-03-19 -> 7자리 , 2017-03 추출
df['month'] = df['create_date'].apply(lambda x: x[:7])

# 종류별 개수출력, 월별 거래 횟수를 계산하여 출력.
df['month'].value_counts()

# 일별 거래 횟수를 계산하여 그래프로 출력.
# to_datetime 문자타입 -> date타입으로 변환
# df_day = pd.to_datetime(df['create_date'].apply(lambda x: x[:10])).value_counts()
# df_day.plot()
# plt.show()

# 가격의 분포를 그래프로 탐색.
# 60만원 아래에서 거래가 형성되어 있음.
# df['price'].hist(bins="auto")
# plt.show()

# 핸드폰 기종(phone_model)별 가격의 평균과 표준편차를 계산
# transform함수 lambda함수를 실행해서 값을 리턴해줌. 
# <예제>df_modified = df.transform(func = lambda x : x + 10)
# print(df.groupby('phone_model')['price'].mean())
df_price_model_mean = df.groupby('phone_model')['price'].transform(lambda x: np.mean(x))
df_price_model_std = df.groupby('phone_model')['price'].transform(lambda x: np.std(x))

# 이를 바탕으로 모든 데이터의 z-score를 계산
# 이는 해당 데이터의 가격이 기종별 평균에 비해 어느정도로 높거나 낮은지를 알 수 있게 하는 점수.
# z점수출력 - z score
df_price_model_z_score = (df['price'] - df_price_model_mean) / df_price_model_std

# 그래프 출력 - 정규분포를 따름.
# df_price_model_z_score.hist(bins="auto")
# plt.show()


# 출고가 그래프 - factory_price 피처의 분포를 탐색
# df['factory_price'].hist(bins="auto")
# plt.show()

# 출고가와 중고가 의 상관관계 확인
# factory_price와 price 를 scatter plot으로 출력하여, 상관관계를 확인.
# df.plot.scatter(x='factory_price', y='price')
# plt.show()

# 폰모델별 개수 - 기종별 총 거래 데이터 개수를 집계
model_counts = df['phone_model'].value_counts()
print(model_counts.describe())

# 기종별 총 거래 데이터 개수를 상자 그림으로 살펴봄.
# 100건 미만으로 거래량이 존재
# plt.boxplot(model_counts)
# plt.show()


# 물가 피처 탐색
# print(df['price_index'].value_counts())


# ---------------------------------------------------------
#        중고가 예측 - 랜덤포레스트
# ---------------------------------------------------------
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# 데이터 전처리 
df = df[['price', 'phone_model', 'factory_price', 'maker', 'price_index', 'month']]
# 원핫 인코딩 작업
df = pd.get_dummies(df, columns=['phone_model', 'maker', 'month'])
data = df[df.columns.difference(['price'])]
# data = df.loc[:, df.columns != 'price']
label = df['price']

# train,test데이터 분리
train_data,test_data,train_label,test_label = train_test_split(data,label,random_state=20)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


#----------------------------------------------------------------------
# RandomizedSearchCV 오브젝트를 생성하여 모델을 정의합니다.
# from scipy.stats import uniform,randint
# params = {'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005]}
# gs = GridSearchCV(RandomForestRegressor(random_state=42),params,n_jobs=-1)

#----------------------------------------------------------------------
# 알고리즘 선택 - 랜덤 포레스트.  
gs = RandomForestRegressor(n_estimators=1000)
gs.fit(train_data, train_label)

# 예측
train_result = gs.predict(train_data)
test_result = gs.predict(test_data)

# 정확도
train_score = gs.score(train_data,train_label)
print("train_score : ",train_score)
test_score = gs.score(test_data,test_label)
print("train_score : ",test_score)

# 오차범위
mae = mean_absolute_error(test_label,test_result)
print("오차범위 : ",mae)

# -----------------------------------------------------
# 중요도 그래프.
# 특성별 중요도 출력
importances = gs.feature_importances_
# 중요도 정렬 - numpy array정렬
# 예) s = a.argsort()    a = np.array([1.5, 0.2, 4.2, 2.5])
# print(s) [1 0 3 2]
# print(a[s]) [0.2 1.5 2.5 4.2]
indices = np.argsort(importances)[::-1]
plt.bar(range(data.shape[1]), importances[indices])
# plt.show()

# 학습한 모델의 피처 중요도를 출력.
# data컬럼명 factory_price, maker_apple...
# 컬럼명과 중요도 합침, 역순정렬 - 중요도를 가지고 역순정렬
feat_labels = data.columns.tolist()
feature = list(zip(feat_labels, gs.feature_importances_))
print(sorted(feature, key=lambda tup: tup[1], reverse=True)[:10])

# month 피처 중, 영향력이 높은순으로 정렬하여 출력.
# 위에서는 10개 출력, 모두출력하는데, month가 있는 것만 출력
for sorted_feature in sorted(feature, key=lambda tup: tup[1], reverse=True):
    # month글자가 있는 것만 출력 : 0번째 열 ('month_2017-03', 0.017943115800069562)
    if "month" in sorted_feature[0]: 
        print(sorted_feature)


# test_label데이터와 test예측데이터를 가지고 그래프를 그려보면
# 데이터가 일치한지를 알수 있음. 직선에 가까울수록 일치한다라고 판단
plt.scatter(test_label.values, test_result)
plt.show()







