# Pillow 함수사용
from PIL import Image
import numpy as np
# 이미지 데이터를 Average Hash로 변환하기 --- (※1)
# average Hash변환
# 이미지 크기를 8x8로 축소
# 색을 그레이스케일로 변환
# 이미지의 각 픽셀의 평균을 계산
# 각 픽셀의 어두운 정도가 평균보다 크면 1, 평균보다 작으면 0으로 입력

# pip install Pillow

def average_hash(fname, size = 16):
    # Pillow 함수 호출
    img = Image.open(fname) # 이미지 데이터 열기---(※2)
    # convert : L지정 - 그레이스케일, 1을 지정 - 이진화, 그외지정 : RGB,RGBA,CMYK 모드변경
    img = img.convert('L') # 그레이스케일로 변환하기 --- (※3)
    img = img.resize((size, size), Image.ANTIALIAS) # 리사이즈하기 --- (※4)
    pixel_data = img.getdata() # 픽셀 데이터 가져오기 --- (※5)
    pixels = np.array(pixel_data) # Numpy 배열로 변환하기 --- (※6)
    print(pixels)
    # raise Exception('강제예외발생')
    pixels = pixels.reshape((size, size)) # 2차원 배열로 변환하기 --- (※7)
    print(pixels) # 16X16
    avg = pixels.mean() # 평균 구하기 --- (※8)
    print(avg) # 57.625
    diff = 1 * (pixels > avg) # 평균보다 크면 1, 작으면 0으로 변환하기 --- (※9)
    return diff
# 이진 해시로 변환하기 --- (※10)
def np2hash(ahash):
    bhash = []
    for nl in ahash.tolist():
        sl = [str(i) for i in nl]
        s2 = "".join(sl)
        i = int(s2, 2) # 이진수를 정수로 변환하기
        bhash.append("%04x" % i)
    return "".join(bhash)

# --------------------------------------------------------------------
# Average Hash 함수호출
ahash = average_hash('deeplearning/tower.jpg')

# 이전 실습까지 28x28픽셀 = 784개 입력데이터 이미지
# 이진코드로 출력 - 이미지 218/255로 나눠서 데이터를 가지고 있으면 
# 딥러닝 구현 가능
print(ahash)

print(ahash.reshape(1,-1))


# 해쉬코드로 출력
# print(np2hash(ahash))