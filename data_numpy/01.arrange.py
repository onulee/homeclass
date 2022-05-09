import numpy as np

array = np.arange(0,10)
np.save('arrange1.npy',array)

result = np.load('arrange1.npy')
print(result)