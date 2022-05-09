class Myclass(object):
    def __init__(self,stu_num=None,kor=0,eng=0,math=0):
        self.stu_num=stu_num
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg= self.total/3.0
        
stu1 = Myclass(1,100)

# stu1.stu_num=5

print("학생번호 :",stu1.stu_num)        
print("국어점수 :",stu1.kor)        
print("합계 :",stu1.total)        
print("평균 :",stu1.avg)        