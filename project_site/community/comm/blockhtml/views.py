from django.shortcuts import render
import cx_Oracle as ora

# Create your views here.
def main(request):
    return render(request,'main.html')

def notice_list(request):
    ## import cx_Oracle as ora
    ## 오라클 연결 
    conn = ora.connect('c##ora_user1/1111@localhost:1521/xe')
    print(conn.version)
    cursor = conn.cursor()
    print(cursor)
    #SQL문 작성
    sql_insert ='insert into board values(board_seq.nextVal)'
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