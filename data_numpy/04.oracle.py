#ora_user/1234@localhost:1521/xe
# employees 테이블의 데이터를 파이썬 프로그램으로 읽어서 리턴

# cx_Oracle.makedsn : 오라클에 대한 주소 정보
# cx_Oracle.connect : 오라클 접속 유저 정보
# db.cursor : 데이터 담을 메모리의 이름을 선언
# cursor.execute : SQL의 결과가 cursor 메모리를 담는다.
# cursor.fetchall : 메모리에 담긴 데이터를 한 행씩 fetch 한다. 전부 all.
# cursor.description : 데이터의 칼럼명을 추출합니다.


import cx_Oracle

def myConn():
    conn = cx_Oracle.connect("ora_user/1234@localhost:1521/XE") # 오라클 접속 
    return conn

def mySelect():
    conn = myConn() 
    cursor=conn.cursor()
    sql = "select * from board"
    rows = cursor.execute(sql)	
    for row in rows:
        print(row[7])
    cursor.close()
    conn.close()
    
def myInsert():
    conn = myConn() 
    cursor=conn.cursor()
    sql = "insert into board values(board_seq.nextval,:1,:2,:3,board_seq.currval,:4,:5,sysdate,:6,:7)"
    cursor.execute(sql,('게시글제목4','게시글내용4','이순신',0,0,'4.jpg',0))	
    print('insert : ',cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()
    
def myUpdate():
    conn = myConn() 
    cursor=conn.cursor()
    sql = "update board set btitle=:1 where bid=:2"
    cursor.execute(sql,('게시글제목44','41'))	
    print('update : ',cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()
    
def myDelete():
    conn = myConn() 
    cursor=conn.cursor()
    sql = "delete board where bid=:1"
    cursor.execute(sql,('41'))	
    print('delete : ',cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()
    


conn = myConn()
cursor=conn.cursor()
rows = cursor.execute("select * from board")
for row in rows:
    print(row[7])
    
# myInsert() 
mySelect()  
myUpdate() 



