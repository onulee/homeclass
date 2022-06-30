import numpy as np
from pandas import pd

countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                'Austria', 'France', 'Poland', 'China', 'Korea', 
                'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

olympic_df = {'country_name':countries,
                        'gold': gold,
                        'silver': silver,
                        'bronze': bronze}
df = pd.DataFrame(olympic_df)
medal_cnt = df[['gold','silver','bronze']]
points = np.dot(medal_cnt, [4,2,1])
                
olympic_points = {'country_name': countries,
                    'points': points}
olympic_points_df = pd.DataFrame(olympic_points)

print (olympic_points_df)



# arr5 = np.arange(100).reshape(10,10)
# left,right = np.split(arr5,[3],axis=1)
# print(left)
# print(right)



# arr2 = np.arange(1,12,2).reshape(3,2)
# print(arr2)
# arr3 = np.arange(2,13,2).reshape(3,2)
# print(arr3)
# arr4 = np.concatenate([arr2,arr3],axis=0)
# print(arr4)




# arr5= np.arange(1,10).reshape(3,3)
# arr5[1] = arr5[1]*2
# arr5[2] = arr5[2]*2
# print(arr5)



# arr3= np.arange(1,7).reshape(2,3)
# arr4 = np.arange(7,13).reshape(3,2)
# print(arr3.dot(arr4))



# arr1 = np.array([[1,1], [0,1]])
# arr2 = np.array([[2,0], [3,4]])
# print(arr1 * arr2) 
# print(arr1.dot(arr2))



# arr = np.arange(1,10).reshape(3,3)
# print(arr.sum(axis=0))
# print(arr.sum(axis=1))



# arr = np.arange(1,10).reshape(3,3)
# print(arr[ : ,0], arr[ : , 1],arr[ : ,2])

# print(arr)




# arr = np.arange(1,10).reshape(3,3)
# print(arr[0],arr[1],arr[2])



# arr = [[0,1,2],[3,4,5]]    # [ 0   ,   1  ]
# len_row = len(arr)     # row : 2   [ (),() ] - 안에 2개
# len_col = len(arr[0])  # col : 3    [0,1,2] - 안에 3개
# print(len_row)
# print(len_col)

