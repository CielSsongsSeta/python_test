<<<<<<< HEAD
class 학생 :
    이름 = ''
    번호 = 0
    키 = 0.0
    def __init__(self, 이름, 번호, 키) :
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키
    def 학생정보보기(self):
        print(self.이름, self.번호, self.키)
    def 학생정보입력(self):
        self.이름 = input('이름입력: ')
        self.번호= int(input('번호입력: '))
        self.키= float(input('키 입력: '))
        #print(self.이름, self.번호, self.키)
#'짱구', 4, 174.1
철수 = 학생('김철수', 1, 177.7)
영희 = 학생('박영희', 2, 155.5)
짱구 = 학생('신짱구', 3, 173.3) 

철수.학생정보보기()
영희.학생정보보기()
짱구.학생정보보기()

짱구.학생정보입력()
=======
class 학생 :
    이름 = ''
    번호 = 0
    키 = 0.0
    def __init__(self, 이름, 번호, 키) :
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키
    def 학생정보보기(self):
        print(self.이름, self.번호, self.키)
    def 학생정보입력(self):
        self.이름 = input('이름입력: ')
        self.번호= int(input('번호입력: '))
        self.키= float(input('키 입력: '))
        #print(self.이름, self.번호, self.키)
#'짱구', 4, 174.1
철수 = 학생('김철수', 1, 177.7)
영희 = 학생('박영희', 2, 155.5)
짱구 = 학생('신짱구', 3, 173.3) 

철수.학생정보보기()
영희.학생정보보기()
짱구.학생정보보기()

짱구.학생정보입력()
>>>>>>> ea4ffdb9811163530489334f9c4dfcc2fbe819fb
짱구.학생정보보기()