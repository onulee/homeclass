import numpy as np


# 중복된 원소 제거
array = np.array([1, 1, 2, 3, 3, 3, 1])
print(np.unique(array))



# # 난수의 재연 (실행마다 결과 동일)
# np.random.seed(7)
# print(np.random.randint(0, 10, (2, 3)))



# array = np.linspace(0,10,5)
# print(array)



# # 각 열을 기준으로 정렬
# array = np.array([[5,9,10,3,1],[8,3,4,2,5]])
# print(array)
# array.sort(axis=0)
# print(array)