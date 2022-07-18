import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.model_selection import train_test_split
matplotlib.rcParams['axes.unicode_minus'] = False
from gensim.models.word2vec import Word2Vec
from konlpy.tag import Okt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import imdb
from tensorflow.keras.utils import plot_model

#-----------------------------------------------------------------------
# 모델 불러오기
model = keras.models.load_model('best-cnn-model.h5')
# 모델의 층 객체를 list로 보여줌.
print(model.layers)

conv = model.layers[0]
print(conv.weights[0].shape, conv.weights[1].shape)