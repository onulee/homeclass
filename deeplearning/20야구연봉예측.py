import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.preprocessing import StandardScaler
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error  # 실제 값과 예측 값의 차이를 제곱해 평균화
from math import sqrt


picher_file_path = 'deeplearning/picher_stats_2017.csv'
batter_file_path = 'deeplearning/batter_stats_2017.csv'
picher = pd.read_csv(picher_file_path)
# batter = pd.read_csv(batter_file_path)

# 각선수별 경기정보,승률,연봉 상위5개 출력
print(picher.head())

# data,label을 분리
# 선수명   팀명   승   패  세  홀드  블론  경기  선발  ...  BABIP  LOB%   ERA  RA9-WAR   FIP  kFIP   WAR 
# 연봉(2018)  연봉(2017)

# 컬럼출력
print(picher.columns)

# df사이즈 출력
print(picher.shape)
# (152, 22)

# 연봉에 대한 정보 - 개수,평균,표준편차,최소값,최대값
print(picher['연봉(2018)'].describe())


#--------------------------------------------------------- 
# # 히스토그램 그래프 출력
# # hist:히스토그램 그래프, bins : 가로축 구간의 개수 ,총 100개
# # picher['연봉(2018)'].hist(bins=100) # 2018년 연봉 분포를 출력.
# plt.hist(picher['연봉(2018)'],bins=100)
# plt.show()
# # boxplot 그래프, 박스권 안은 기준 내의 데이터 값, 밖의 그래프는 기준 밖의 값
# picher.boxplot(column=['연봉(2018)']) # 연봉의 Boxplot을 출력.
# plt.show()

#---------------------------------------------------------
# 최종 column 확인 - 데이터를 가지고 그래프로 확인
picher_features_df = picher[['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR',
       '연봉(2018)', '연봉(2017)']]

# ######### 함수생성 #########
# # 함수생성, 피처 각각에 대한 histogram 그래프 출력.
# def plot_hist_each_column(df):
#     plt.rcParams['figure.figsize'] = [20, 16]
#     fig = plt.figure(1)
    
#     # df의 column 갯수 만큼의 subplot을 출력 : column 20개
#     # 예) 1행2개의 그래프에서 첫번째에 그래프 출력
#     # plt.subplot(1, 2, 1)    # nrows=1, ncols=2, index=1
#     for i in range(len(df.columns)):
#         ax = fig.add_subplot(5, 5, i+1)
#         plt.hist(df[df.columns[i]], bins=50)
#         ax.set_title(df.columns[i])
#     plt.show()

# # 그래프 함수호출 - 컬럼별 그래프 20개 생성   
# # plot_hist_each_column(picher_features_df)    
# #--------------------------------------------------------- 


# 투수의 연봉 예측하기
# 피처들의 단위 맞춰주기 - 정규화,표준화작업
# pandas 형태로 정의된 데이터를 출력할 때, scientific-notation이 아닌 float 모양으로 출력되게 해줌
pd.options.mode.chained_assignment = None

######### 함수생성 #########
# 정규화, 표준화 작업
# 각 컬럼의 데이터 정규화 작업을 함. 피처 각각에 대한 scaling을 수행하는 함수를 정의.
# 데이터-평균/표준편차 , ss = StandardScaler() 사용해도 됨.
def standard_scaling(df, scale_columns):
    for col in scale_columns:
        series_mean = df[col].mean()
        series_std = df[col].std()
        df[col] = df[col].apply(lambda x: (x-series_mean)/series_std)
    return df

# 피처 각각에 대한 scaling을 수행.
scale_columns = ['승', '패', '세', '홀드', '블론', '경기', '선발', '이닝', '삼진/9',
       '볼넷/9', '홈런/9', 'BABIP', 'LOB%', 'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR', '연봉(2017)']
# 함수호출 - 전체데이터 picher
picher_df = standard_scaling(picher, scale_columns)
# print(picher_df)  # 정규화작업을 통한 데이터 변경

# # 컬럼명 변경 - label값의 컬럼명 변경
picher_df = picher_df.rename(columns={'연봉(2018)': 'y'})
print(picher_df.head(5))

# [피처들의 단위 맞춰주기 : one-hot-encoding]
# 데이터는 모두 정수 또는 실수 숫자여야 함. - 팀명은 글자이기에 000010000
# 팀명 피처를 one-hot encoding으로 변환
# get_dummies 팀명의 개수로 0000100 원핫인코딩으로 만들어줌.
# 알고리즘에 사용할 데이터를 완성
team_encoding = pd.get_dummies(picher_df['팀명'])
picher_df = picher_df.drop('팀명', axis=1)  # 팀명컬럼 삭제
picher_df = picher_df.join(team_encoding) # 
# 상위5개 출력
print(team_encoding.head(5))

# # 피처 상위 5개 출력
# print(picher_df.head())


# -----------------------------------------------------------------
# [선형회귀 분석 사용]
# 학습 데이터와 테스트 데이터로 분리
# data : 선수명,y를 제외한 모든 컬럼, 
# label = y        # (columns={'연봉(2018)': 'y'}) 이름 변경했음
X = picher_df[picher_df.columns.difference(['선수명', 'y'])]  
y = picher_df['y']    
# train,test 데이터 분리                                               
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19)

# # 선형회귀 (회귀 모델 학습)
lr = LinearRegression()
# 훈련
model = lr.fit(X_train, y_train)

# 기울기, y절편 학습된 계수를 출력.
print(lr.coef_,lr.intercept_)  # 28개 : 2개는 label, 총컬럼수 30개
# score 확인 : 회귀 분석 모델을 평가.
print(model.score(X_train, y_train)) # train R2 score를 출력
print(model.score(X_test, y_test)) # test R2 score를 출력  # score : 0.8860171644977815
print("-"*50)

# 컬럼출력
print(picher_df.columns)


# -------------------------------------------------------------
#              정확도 확인, 평가를 하는 부분 ( 제외 가능 )  
# -------------------------------------------------------------


# 1. 선형회귀의 정확도를 summary로 요약을 해줌.
# -------------------------------------------------------------
# 예측 모델 평가 - 예측한 모델이 데이터를 잘 포함하고 있는지 확인가능
# R-squared: 0.928 선형회귀의 선과 데이터가 잘 붙어있는지 확인가능
# Prob (F-statistic): 7.70e-42 : 선형회귀가 잘 수행이 되었는지 확인가능, 수치가 낮을수록 좋음.
# P>|t| 0에 가까울수록 모델에 의미있는 데이터가 됨.
# import statsmodels.api as sm
# # statsmodel 라이브러리로 회귀 분석을 수행.
# X_train = sm.add_constant(X_train)
# model = sm.OLS(y_train, X_train).fit()
# print(model.summary())

# # # 회귀 계수를 리스트로 반환합니다.
# coefs = model.params.tolist()
# coefs_series = pd.Series(coefs)

# # # 변수명을 리스트로 반환합니다.
# x_labels = model.params.index.tolist()

#--------------------------------------------------------- 
# 회귀 계수를 그래프 출력.
# ax = coefs_series.plot(kind='bar')
# ax.set_title('feature_coef_graph')
# ax.set_xlabel('x_features')
# ax.set_ylabel('coef')
# ax.set_xticklabels(x_labels)
# plt.show()

# 2. 정확도 확인 : [예측 모델의 평가]
# 학습 데이터와 테스트 데이터로 분리.
# X = picher_df[picher_df.columns.difference(['선수명', 'y'])]
# y = picher_df['y']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19)

# # 회귀 분석 모델을 학습
# lr = LinearRegression()
# model = lr.fit(X_train, y_train)

# # 회귀 분석 모델을 평가.
# print(model.score(X_train, y_train)) # train R2 score를 출력합니다.
# print(model.score(X_test, y_test)) # test R2 score를 출력합니다.

# # 회귀 분석 모델을 평가합니다.
# y_predictions = lr.predict(X_train)
# print(sqrt(mean_squared_error(y_train, y_predictions))) # train RMSE score를 출력합니다.
# y_predictions = lr.predict(X_test)
# print(sqrt(mean_squared_error(y_test, y_predictions))) # test RMSE score를 출력합니다.


# [피처들의 상관관계 분석]
import seaborn as sns

# 피처간의 상관계수 행렬을 계산.
corr = picher_df[scale_columns].corr(method='pearson')
show_cols = ['win', 'lose', 'save', 'hold', 'blon', 'match', 'start', 
             'inning', 'strike3', 'ball4', 'homerun', 'BABIP', 'LOB', 
             'ERA', 'RA9-WAR', 'FIP', 'kFIP', 'WAR', '2017']

#--------------------------------------------------------- 
# corr 행렬 히트맵을 시각화합니다.
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
# 회귀모델에 영향이 높은 컬럼들을 확인해서 제거
from statsmodels.stats.outliers_influence import variance_inflation_factor

# 피처마다의 VIF 계수를 출력.
# 회귀모델에 영향이 높은 컬럼들을 확인해서 제거
# VIF Factor 가 100 이 넘어가면 모델에 너무 높은 영향을 줌.
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns
print(vif.round(1))


##################################################

# 영향력이 너무 높은 것은 제외하고 다시 선형회귀 알고리즘 실행

##################################################

# 피처를 재선정
X = picher_df[['FIP', 'WAR', '볼넷/9', '삼진/9', '연봉(2017)']]
y = picher_df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=19)

# 모델을 학습합니다.
lr = LinearRegression()
model = lr.fit(X_train, y_train)

# 결과를 출력합니다.
print(model.score(X_train, y_train)) # train R2 score를 출력합니다.
print(model.score(X_test, y_test)) # test R2 score를 출력합니다.

# 회귀 분석 모델을 평가합니다.
y_predictions = lr.predict(X_train)
print(sqrt(mean_squared_error(y_train, y_predictions))) # train RMSE score를 출력합니다.
y_predictions = lr.predict(X_test)
print(sqrt(mean_squared_error(y_test, y_predictions))) # test RMSE score를 출력합니다.

# 피처마다의 VIF 계수를 출력합니다.
X = picher_df[['FIP', 'WAR', '볼넷/9', '삼진/9', '연봉(2017)']]
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns

# 10을 넘는 vif가 없음. 고르게 영향을 미치고 있다고 판단
print(vif.round(1))


#################################################
#    <Step4. 시각화> : 분석 결과의 시각화
#################################################
# 2018년 연봉을 예측하여 데이터프레임의 column으로 생성.
X = picher_df[['FIP', 'WAR', '볼넷/9', '삼진/9', '연봉(2017)']]
predict_2018_salary = lr.predict(X)
picher_df['예측연봉(2018)'] = pd.Series(predict_2018_salary)

# 원래의 데이터 프레임을 다시 로드합니다.
picher = pd.read_csv(picher_file_path)
picher = picher[['선수명', '연봉(2017)']]

# 원래의 데이터 프레임에 2018년 연봉 정보를 합칩니다.
result_df = picher_df.sort_values(by=['y'], ascending=False)
result_df.drop(['연봉(2017)'], axis=1, inplace=True, errors='ignore')
result_df = result_df.merge(picher, on=['선수명'], how='left')
result_df = result_df[['선수명', 'y', '예측연봉(2018)', '연봉(2017)']]
result_df.columns = ['선수명', '실제연봉(2018)', '예측연봉(2018)', '작년연봉(2017)']

# # 재계약하여 연봉이 변화한 선수만을 대상으로 관찰합니다.
result_df = result_df[result_df['작년연봉(2017)'] != result_df['실제연봉(2018)']]
result_df = result_df.reset_index()
result_df = result_df.iloc[:10, :]
print(result_df.head(10))

# 선수별 연봉 정보(작년 연봉, 예측 연봉, 실제 연봉)를 bar 그래프로 출력합니다.
result_df.plot(x='선수명', y=['작년연봉(2017)', '예측연봉(2018)', '실제연봉(2018)'], kind="bar")
plt.show()


