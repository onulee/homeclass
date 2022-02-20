# 3. Index
# 데이터에 접근할 수 있는 주소 값
# DataFrame 객체생성 (Index 지정)
# index 이름 설정, # index 초기화
import pandas as pd

data = {
    '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
    '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

# (Index 지정)
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])

# index 출력
print(df.index)

# index 이름 설정
df.index.name = '지원번호'
print(df)

# index 초기화
df.reset_index()  # 이 명령어일때만 가능
print(df)

# index 삭제 - 원래 쓰던 '지원번호' 인텍스 삭제
# 실제 반영이 된것이 아니기에 다시 출력하면 나타남
df.reset_index(drop=True,inplace=True)  # 이 명령어 일때만 가능
print(df)

# 실제 데이터에 바로 반영
# df.reset_index(drop=True, inplace=True) 
# print(df)