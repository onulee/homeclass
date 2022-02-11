import pandas as pd
from matplotlib import pyplot as plt
data={
    'year ' : [2016,2017,2018],
    'GDP rate' : [2.8,3.1,3.0],
    'GDP' : ['1.637M','1.73M','1.83M']
}

df=pd.DataFrame(data)
print(df)
