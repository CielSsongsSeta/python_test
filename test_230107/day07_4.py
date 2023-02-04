class c1 :
    def AbsSum(self, n1,n2) :
        result = 0
        if n1 < 0 :
            n1 = n1 * -1
        if n2 < 0 :
            n2 = n2 * -1
        self.n1 = n1
        self.n2 = n2
        result = n1 + n2
        return result
    def Last(self) :
        print(self.n1+self.n2)
    # 생성자 __init__ : 객체화하는 순간에 사용될 메서드
    def __init__(self) :
        print('회사프로그램 객체화를 성공했습니다!!')
    def __init__(self,n1,n2):
        self.AbsSum(n1,n2)

a = c1(3,5)
a.Last()
# 클래스 이름 옆에 있는 ()는 __init__를 사용하는 코드
b = c1(5,-2)
b.Last()