from sklearn import svm
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from scipy.special import expit
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
from scipy.special import softmax

df = pd.read_csv('deeplearning/iris(150).csv')
print(df['Species'].unique()) # 중복된 row1개만 출력

data = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
# df['Species'] = df['Species'].apply(nameChange)  # 함수호출, 변경값:df 적용
label = df['Species']

data_numpy = np.array(data) 
label_numpy = np.array(label) 


 # 테스트 데이터 30%
x_train, x_test, y_train, y_test = train_test_split(data_numpy, label_numpy, test_size=0.3)
print(len(x_train))
print(len(x_test))
print(len(y_train))
print(len(y_test))

# 학습 진행
forest = RandomForestClassifier(n_estimators=100)
forest.fit(x_train, y_train)

# 예측
y_pred = forest.predict(x_test)
print(y_pred)
print(list(y_test))

# 정확도 확인
print('정확도 :', metrics.accuracy_score(y_test, y_pred))