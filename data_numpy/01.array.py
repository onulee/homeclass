import numpy as np

# list_data = [0,1,2,3,4]
# arr = np.array(list_data)
# print(arr)

# print(arr.shape)
# print(arr.size)
# print(arr.dtype)

# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# arr = np.array(lst)
 
# # 슬라이스
# a = arr[0:1, 0:2]
# print(a)

# lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# a = np.array(lst)
 
# bool_indexing_array = np.array([
#     [False,  True, False],
#     [True, False,  True],
#     [False,  True, False]
# ])
 
# n = a[bool_indexing_array];
# print(n) 

# array1 = np.arange(4).reshape(2, 2)
# print(array1)
# array2 = np.arange(2)
# print(array2)
# array3 = array1 + array2

# print(array3)

import numpy as np

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
a = np.array(lst)
 
bool_indexing_array = np.array([
    [False,  True, False],
    [True, False,  True],
    [False,  True, False]
])
 
n = a[bool_indexing_array];
print(n)

