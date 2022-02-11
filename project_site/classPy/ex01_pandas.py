import pandas as pd
temp=pd.Series([-20,-10,10,20]) # index 사용하지 않을때
print(temp)
print(temp[0])

temp2=pd.Series([-20,-10,10,20],index=['Jan','Feb','Mar','Apr']) #index사용할때
print(temp2)
print(temp2['Jan'])
#print(temp2['June']) 없는 데이터 넣으면 오류

print(temp2['Feb'])