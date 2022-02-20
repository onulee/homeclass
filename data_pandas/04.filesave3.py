# 4. 파일저장 및 열기
# csv파일 열기

import pandas as pd

# csv파일 열기
df = pd.read_csv('score.csv')

# 1번째 row skip후 출력 : 이름 학교 키... 부분 삭제
df=pd.read_csv('score.csv',skiprows=1) 

# 1,3,5 번째 row skip후 출력
df=pd.read_csv('score.csv',skiprows=[1,3,5]) 

# 지정된 개수 만큼 출력
df=pd.read_csv('score.csv',nrows=4)

# 처음2row 무시, 이후에 4row를 가져옴
# 상단 타이틀
df=pd.read_csv('score.csv',skiprows=2, nrows=4)





