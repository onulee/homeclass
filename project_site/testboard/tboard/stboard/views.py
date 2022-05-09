from django.shortcuts import render
import cx_Oracle as ora
import pandas as pd
from stboard.models import Board

# db연결함수로 정의
def connections():
    try:
        conn= ora.connect('system/1234@localhost:1521/xe')
        # cursor = conn.cursor()
    except Exception as e:
        msg="예외발생"
        print(msg)
    return conn


# tpage board게시판리스트
def tpage(request):
    ## import cx_Oracle as ora
    ## 오라클 연결
    df = pd.read_excel('C:/pyFolder/js_work/board_code.xlsx',usecols='A:D',dtype={0:int,1:str,2:str,3:str})
    # df1 = df[['bid','btitle','bname','bgroup']]
    rows=[ ]
    for x in df.to_records(index=False):
        row=[ int(x[0]),x[1],x[2],x[3] ]
        rows.append(row)
    
    conn = connections()
    print(conn.version) # 18.4.0.0.0 
    cursor = conn.cursor()   
    print(cursor) # <cx_Oracle.Cursor on <cx_Oracle.Connection to c##ora_user1@localhost:1521/xe>>
    
    # oracle db 에 저장
    cursor.execute('delete from board')
    board_query = 'insert into board(bid,btitle,bname,bgroup) values(:1,:2,:3,:4)'
    cursor.executemany(board_query,rows)
    conn.commit()
    
    cursor.execute('select count(*) from board')
    cnt = cursor.fetchone()
    print('insert 건수 : ',cnt)
    
    cursor.close()
    conn.close()
    return render(request,'blist.html')



# tpage board게시파리스트2
def tpage2(request):
    # conn = connections()
    # query ='select * from score' 
    # df = pd.read_sql_query(query,conn)
    # print(df)
    # df.to_sql('score2',con=connections(), if_exists='append', chunksize=1000, index=False, method='multi')
    # conn.close()  
    bid=1
    qs = Board.objects.all()
    print(qs.query)
    context={'blist':qs}
    
    return render(request,'blist2.html',context)

