from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split

# 1개의 RGB컬러를 변경
with open("deeplearning/tower.jpg","rb") as file:
    # hash코드로 오픈
    img = Image.open(file)
    # 컬러변환
    img = img.convert("RGB")
    # 사이즈 변경
    img = img.resize((64, 64))
    # 배열로 변경
    data = np.asarray(img)
    
    # numpy배열로 변경
    # 500개이미지 hash코드로 변경후 저장가능
    np.save("5obj.npy", data)
    # np.save("./image/5obj.npy", data)
    
    print(len(list(data)))
    print(len(list(data[0])))
    print(data[0][0])
    img.save("test.jpg")
 