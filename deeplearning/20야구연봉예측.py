import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error  # 실제 값과 예측 값의 차이를 제곱해 평균화
from math import sqrt


picher_file_path = 'deeplearning/picher_stats_2017.csv'
batter_file_path = 'deeplearning/batter_stats_2017.csv'
picher = pd.read_csv(picher_file_path)
# batter = pd.read_csv(batter_file_path)

# 각선수별 경기정보,승률,연봉 상위5개 출력
print(picher.head())

# 컬럼출력
print(picher.columns)

# df사이즈 출력
print(picher.shape)

# 연봉에 대한 정보 - 개수,평균,표준편차,최소값,최대값
print(picher['연봉(2018)'].describe())


#--------------------------------------------------------- 
# 그래프 출력
# picher['연봉(2018)'].hist(bins=100) # 2018년 연봉 분포를 출력.
# plt.show()
# picher.boxplot(column=['연봉(2018)']) # 연봉의 Boxplot을 출력.
# plt.show()

# 회귀 분석에 사용할 피처 살펴보기
picher_features_df = picher[['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
       '연봉(2018)', '연봉(2017)']]

print(picher_features_df)

#### 함수생성 ####
# 함수생성, 피처 각각에 대한 histogram 그래프 출력.
def plot_hist_each_column(df):
    plt.rcParams['figure.figsize'] = [20, 16]
    fig = plt.figure(1)
    
    # df의 column 갯수 만큼의 subplot을 출력합니다.
    for i in range(len(df.columns)):
        ax = fig.add_subplot(5, 5, i+1)
        plt.hist(df[df.columns[i]], bins=50)
        ax.set_title(df.columns[i])
    plt.show()

#---------------------------------------------------------    
# 그래프 함수호출 - 컬럼별 그래프 20개 생성   
# plot_hist_each_column(picher_features_df)    



# 투수의 연봉 예측하기
# 피처들의 단위 맞춰주기 - 정규화,표준화작업
# pandas 형태로 정의된 데이터를 출력할 때, scientific-notation이 아닌 float 모양으로 출력되게 해줌
pd.options.mode.chained_assignment = None

#### 함수생성 ####
# 피처 각각에 대한 scaling을 수행하는 함수를 정의합니다.
def standard_scaling(df, scale_columns):
    for col in scale_columns:
        series_mean = df[col].mean()
        series_std = df[col].std()
        df[col] = df[col].apply(lambda x: (x-series_mean)/series_std)
    return df

# 피처 각각에 대한 scaling을 수행.
scale_columns = ['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR', '연봉(2017)']
# 함수호출
picher_df = standard_scaling(picher, scale_columns)

# 컬럼명 변경 
picher_df = picher_df.rename(columns={'연봉(2018)': 'y'})
print(picher_df.head(5))

# [피처들의 단위 맞춰주기 : one-hot-encoding]
# 팀명 피처를 one-hot encoding으로 변환합니다.
team_encoding = pd.get_dummies(picher_df['팀명'])
picher_df = picher_df.drop('팀명', axis=1)
picher_df = picher_df.join(team_encoding)
# 상위5개 출력
print(team_encoding.head(5))

# 피처 상위 5개 출력
print(picher_df.head())


# -----------------------------------------------------------------
# [회귀 분석 적용하기]
# 학습 데이터와 테스트 데이터로 분리
X = picher_df[picher_df.columns.difference(['선수명', 'y'])]
y = picher_df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19)

# 선형회귀 (회귀 모델 학습)
lr = linear_model.LinearRegression()
# 훈련
model = lr.fit(X_train, y_train)

# 기울기, y절편 학습된 계수를 출력.
print(lr.coef_,lr.intercept_)  # 28개 : 2개는 label, 총컬럼수 30개

# 컬럼출력
print(picher_df.columns)


# -------------------------------------------------------------
# 예측 모델 평가
import statsmodels.api as sm
# statsmodel 라이브러리로 회귀 분석을 수행.
X_train = sm.add_constant(X_train)
model = sm.OLS(y_train, X_train).fit()
print(model.summary())

# 회귀 계수를 리스트로 반환합니다.
coefs = model.params.tolist()
coefs_series = pd.Series(coefs)

# 변수명을 리스트로 반환합니다.
x_labels = model.params.index.tolist()

#--------------------------------------------------------- 
# 회귀 계수를 그래프 출력.
# ax = coefs_series.plot(kind='bar')
# ax.set_title('feature_coef_graph')
# ax.set_xlabel('x_features')
# ax.set_ylabel('coef')
# ax.set_xticklabels(x_labels)
# plt.show()

# [예측 모델의 평가]
# 학습 데이터와 테스트 데이터로 분리.
X = picher_df[picher_df.columns.difference(['선수명', 'y'])]
y = picher_df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19)

# 회귀 분석 모델을 학습
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

# 회귀 분석 모델을 평가합니다.
print(model.score(X_train, y_train)) # train R2 score를 출력합니다.
print(model.score(X_test, y_test)) # test R2 score를 출력합니다.

# 회귀 분석 모델을 평가합니다.
y_predictions = lr.predict(X_train)
print(sqrt(mean_squared_error(y_train, y_predictions))) # train RMSE score를 출력합니다.
y_predictions = lr.predict(X_test)
print(sqrt(mean_squared_error(y_test, y_predictions))) # test RMSE score를 출력합니다.


# [피처들의 상관관계 분석]
import seaborn as sns

# 피처간의 상관계수 행렬을 계산.
corr = picher_df[scale_columns].corr(method='pearson')
show_cols = ['win', 'lose', 'save', 'hold', 'blon', 'match', 'start', 
             'inning', 'strike3', 'ball4', 'homerun', 'BABIP', 'LOB', 
             'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR', '2017']

# corr 행렬 히트맵을 시각화합니다.
plt.rc('font', family='NanumGothicOTF')
sns.set(font_scale=1.5)
hm = sns.heatmap(corr.values,
            cbar=True,
            annot=True, 
            square=True,
            fmt='.2f',
            annot_kws={'size': 15},
            yticklabels=show_cols,
            xticklabels=show_cols)

plt.tight_layout()
plt.show()

# [회귀분석 예측 성능을 높이기 위한 방법 : 다중공선성 확인]
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 피처마다의 VIF 계수를 출력합니다.
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns
print(vif.round(1))





