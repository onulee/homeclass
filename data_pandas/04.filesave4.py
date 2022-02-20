# 4. 파일저장 및 열기
# 텍스트(.txt)파일 열기
import pandas as pd

# txt 파일 열기
df = pd.read_csv('score.txt',sep='\t')
# print(df)

# index지정해서 열기
# df = pd.read_csv('score.txt',sep='\t', index_col='지원번호')
# print(df)

df = pd.read_csv('score.txt',sep='\t')
df.set_index('지원번호',inplace=True)
print(df)





