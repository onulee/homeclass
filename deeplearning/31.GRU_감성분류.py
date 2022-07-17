import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import imdb

#----------------------------------------------------------------
# pip install imdby
# 1. 파일 불러오기 - 단어는 500개까지만 출력
(train_input, train_target), (test_input, test_target) = imdb.load_data(
    num_words=500)

# 1-2. 데이터 확인
# 데이터 크기 (25000,) (25000,)
print(train_input.shape, test_input.shape)

# 데이터 확인 [1, 14, 22, 16, 43, 2, 2, 2, 2,.... 너무 좋아요 완전 재미... 
# 첫시작 : 1, 없는 단어 : 2 - 500개의 단어에 없는 단어
print(train_input[0])

# 숫자 길이 - 218  약 218단어로 구성
print(len(train_input[0]))

# 긍정부정 결과label  : [1 0 0 1 0 0 1 0 1 0 1 0 0 0 0 0 1 1 0 1]
print(train_target[:20])


#----------------------------------------------------------------
# 2. 데이터 전처리
# train, test데이터 분리
from sklearn.model_selection import train_test_split

train_input, val_input, train_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)

import numpy as np

# train데이터 길이 확인
lengths = np.array([len(x) for x in train_input])
# 평균길이, 모든값의 중간값 출력
print(np.mean(lengths), np.median(lengths))

# 그래프 그리기
plt.hist(lengths)
plt.xlabel('length')
plt.ylabel('frequency')
plt.show()


#----------------------------------------------------------------
# 3. 단어길이를 줄임 - 속도 개선, 너무 길면 패딩 0의 값이 들어감.
from tensorflow.keras.preprocessing.sequence import pad_sequences

# 평균 178길이를 -> 100길이만 사용 나머지 버림.
train_seq = pad_sequences(train_input, maxlen=100)
# (20000, 100) - 100크기
print(train_seq.shape)

# 첫번째 단어표현 출력 218단어길이 인데 -> 100단어만 사용
# print(len(train_input[0]))
print(train_seq[0])

# 끝에서 10이전 부터 끝까지 출력
# 20  10  10 470 158 -> 20  10  10 470 158 똑같음.
print(train_input[0][-10:])

# 앞쪽이 패딩 0 으로 5개 채워져 있음 - 길이가 95 로 짧음.
print(train_seq[5])

# test데이터도 길이 100까지 줄임.
val_seq = pad_sequences(val_input, maxlen=100)


#----------------------------------------------------------------
# 4. 순환 신경망 선언
from tensorflow import keras

model = keras.Sequential()
#  단어를 실수 벡터로 인코딩, 단어와 단어사이 의미 부여
model.add(keras.layers.Embedding(500, 16, input_length=100))
# LSTM 으로 변경
model.add(keras.layers.GRU(8))
# ----------------------------------------------------------------
# dropout 적용하기
# model.add(keras.layers.LSTM(8, dropout=0.3, return_sequences=True))
# model.add(keras.layers.LSTM(8, dropout=0.3))
# ----------------------------------------------------------------

# model.add(keras.layers.SimpleRNN(8, input_shape=(100, 500)))
model.add(keras.layers.Dense(1, activation='sigmoid'))

# 요약
model.summary()

#----------------------------------------------------------------
# 5. 순환 신경망 훈련 - 인공신경망과 동일함.
# 옵티마이저 - RMSprop 사용 , learning_rate = 0.001
rmsprop = keras.optimizers.RMSprop(learning_rate=1e-4)
model.compile(optimizer=rmsprop, loss='binary_crossentropy', 
              metrics=['accuracy'])
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-simplernn-model.h5', 
                                                save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=3,
                                                  restore_best_weights=True)

history = model.fit(train_oh, train_target, epochs=100, batch_size=64,
                    validation_data=(val_oh, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

# 그래프 그리기
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

# 6. 정확도
score = model.evaluate(val_oh, val_target)
print('loss=', score[0])
print('accuracy=', score[1])

