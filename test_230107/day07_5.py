<<<<<<< HEAD
class Car():
    def __init__(self, Car_Load, Car_Color, Car_Type) :
        self.Car_Load = Car_Load
        self.Car_Color = Car_Color
        self.Car_Type = Car_Type
    def Car_Info(self):
        print(self.Car_Load, self.Car_Color, self.Car_Type)
    def Car_Drive(self) :
        print(self.Car_Load,'가(이) 차를 운전합니다')

'''
<출력형식>
아빠차 = 자동차('아빠','black','gv80')
엄마차 = 자동차('엄마','red','g70')
내차 = 자동차('홍길동','white','k3')

아빠차.Car_Info()
엄마차.Car_Info()
내차.Car_Info()
'''

아빠차 = Car('아빠','black','gv80')
엄마차 = Car('엄마','red','g70')
내차 = Car('홍길동','white','k3')

아빠차.Car_Info()
엄마차.Car_Info()
내차.Car_Info()

=======
class Car():
    def __init__(self, Car_Load, Car_Color, Car_Type) :
        self.Car_Load = Car_Load
        self.Car_Color = Car_Color
        self.Car_Type = Car_Type
    def Car_Info(self):
        print(self.Car_Load, self.Car_Color, self.Car_Type)
    def Car_Drive(self) :
        print(self.Car_Load,'가(이) 차를 운전합니다')

'''
<출력형식>
아빠차 = 자동차('아빠','black','gv80')
엄마차 = 자동차('엄마','red','g70')
내차 = 자동차('홍길동','white','k3')

아빠차.Car_Info()
엄마차.Car_Info()
내차.Car_Info()
'''

아빠차 = Car('아빠','black','gv80')
엄마차 = Car('엄마','red','g70')
내차 = Car('홍길동','white','k3')

아빠차.Car_Info()
엄마차.Car_Info()
내차.Car_Info()

>>>>>>> ea4ffdb9811163530489334f9c4dfcc2fbe819fb
엄마차.Car_Drive()