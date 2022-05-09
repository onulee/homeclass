from django.shortcuts import render
import cx_Oracle as ora
import pandas as pd

# Create your views here.
def main(request):
    return render(request,'main.html')

# db연결함수로 정의
def connections():
    try:
        conn= ora.connect('system/1234@localhost:1521/xe')
        # cursor = conn.cursor()
    except Exception as e:
        msg="예외발생"
        print(msg)
    return conn



# 오라클 연결 1개파일
def ora_list1(request):
    ## import cx_Oracle as ora
    ## 오라클 연결 
    conn = connections()
    print(conn.version)
    cursor = conn.cursor()
    print(cursor)
    #SQL문 작성
    sql_insert ='insert into item_code values(:no,:name)'
    # sql_insert ='insert into board values(board_seq.nextVal,:pwd,:write,:subject,:content,sysdate)'
    # sql_insert
    # #입력값을 쿼리에 바인딩한 후 전송
    cursor.execute(sql_insert,no='0002',name='좋은나라')
    # cursor.execute(sql_insert,pwd=pwdv,write=writev,subject=subjectv,content=contentv)
    # #커서 닫고 commit 해준다.
    cursor.close()
    conn.commit()
    
    return render(request,'notice_list.html')

# 오라클 연결 여러개 파일
def ora_list(request):
    ## import cx_Oracle as ora
    ## 오라클 연결 
    df = pd.read_excel('C:\pyFolder\js_work\score.xlsx',usecols='A:D',dtype={0:str,1:str,2:str,3:str})
    df1 = df[['지원번호','이름','학교','키']]
    rows = [ tuple(x) for x in df1.to_records(index=False) ]
    conn = connections()
    print(conn.version) # 18.4.0.0.0 
    cursor = conn.cursor()   
    print(cursor) # <cx_Oracle.Cursor on <cx_Oracle.Connection to c##ora_user1@localhost:1521/xe>>
    
    # oracle db 에 저장
    cursor.execute('delete from score')
    score_query = 'insert into score values(:1,:2,:3,:4)'
    cursor.executemany(score_query,rows)
    conn.commit()
    
    cursor.execute('select count(*) from score')
    cnt = cursor.fetchone()
    print('insert 건수 : ',cnt)
    
    cursor.close()
    
    return render(request,'notice_list.html')


def notice_list(request):
    ## import cx_Oracle as ora
    ## 오라클 연결 
    conn = ora.connect('c##ora_user1/1111@localhost:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    print(cursor)
    #SQL문 작성
    sql_insert ='insert into item_code values(board_seq.nextVal)'
    # sql_insert ='insert into board values(board_seq.nextVal,:pwd,:write,:subject,:content,sysdate)'
    # sql_insert
    # #입력값을 쿼리에 바인딩한 후 전송
    # cursor.execute(sql_insert,pwd=pwdv,write=writev,subject=subjectv,content=contentv)
    # #커서 닫고 commit 해준다.
    # cursor.close()
    # conn.commit()
    # https://heannim-world.tistory.com/37
    
    return render(request,'notice_list.html')

def notice_read(request):
    return render(request,'notice_read.html')