from tensorflow import keras
from keras.models import Sequential
from keras.layers.core import Dense,Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np
# BMI 데이터를 읽어 들이고 정규화하기 --- (※1)
csv = pd.read_csv("02deep/bmi.csv")
# 몸무게와 키 데이터
csv["weight"] /= 100
csv["height"] /= 200
X = csv[["weight", "height"]]  # --- (※1a)
# 레이블
bclass = {"thin":[1,0,0], "normal":[0,1,0], "fat":[0,0,1]}
y = np.empty((20000,3))
for i, v in enumerate(csv["label"]):
    y[i] = bclass[v]
# 훈련 전용 데이터와 테스트 전용 데이터로 나누기 --- (※2)
X_train, y_train = X[1:15001], y[1:15001]
X_test,  y_test  = X[15001:20001], y[15001:20001] 
# 모델 구조 정의하기 --- (※3)
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=(2,)))
# Dropout : overfitting,overtraining문제를 해결하는 방법
model.add(keras.layers.Dense(512,activation='relu'))
model.add(keras.layers.Dense(512,activation='relu'))
model.add(keras.layers.Dense(3,activation='softmax'))

# ---------------------------------------------------
# 모델생성
# model = Sequential()
# model.add(Dense(512, input_shape=(2,)))
# model.add(Activation('relu'))
# overfitting 문제, overtraining 문제를 해결하는 방법
# model.add(Dropout(0.1))

# model.add(Dense(512))
# model.add(Activation('relu'))
# model.add(Dropout(0.1))

# # 클래스 3개
# model.add(Dense(3))
# model.add(Activation('softmax'))


# 모델 구축하기 --- (※4)
model.compile(loss='categorical_crossentropy',optimizer="adam",metrics='accuracy')
# 데이터 훈련하기 1  --- (※5)
hist = model.fit(
    X_train, y_train,
    batch_size=100,   # batch_size크기
    epochs=20,        # 반복횟수
    validation_split=0.1,
    callbacks=[keras.callbacks.EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1)

# 데이터 훈련하기 2  --- (※5)
# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.h5', save_best_only=True)
# early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,restore_best_weights=True)

# hist = model.fit(X_train, y_train, epochs=20, verbose=0,\
#     validation_data=(X_test,  y_test),callbacks=[checkpoint_cb,early_stopping_cb])



# 테스트 데이터로 평가하기 --- (※6)
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])