class 학생 :
    이름 = ''
    번호 = 0
    키 = 0.0
    몸무게 = 0.0
    def __init__(self, 이름, 번호, 키,몸무게) :
        self.이름 = 이름
        self.번호 = 번호
        self.키 = 키
        self.몸무게 = 몸무게

    def 학생정보보기(self):
        print(self.이름, self.번호, self.키, self.몸무게)

    def 학생정보입력(self):
        self.이름 = input('이름입력: ')
        self.번호= int(input('번호입력: '))
        self.키= float(input('키 입력: '))
        self.몸무게= float(input('몸무게입력: '))

    def __del__(self):
        print('프로그램 종료')

class 학생2(학생) :
    def __del__(self):
        print('프로그램 종료')


class 학생3(학생) :
    def 학생정보보기(self):
        print(f'==이름: {self.이름}, 번호: {self.번호}, 키: {self.키}, 몸무게: {self.몸무게}==')