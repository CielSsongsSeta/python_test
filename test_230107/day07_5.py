class Car():
    def Car_Info(self, Car_Load, Car_Color, Car_Type):
        self.Car_Load = Car_Load
        self.Car_Color = Car_Color
        self.Car_Type = Car_Type
        print(self.Car_Load, self.Car_Color, self.Car_Type)
    def Car_Drive(self) :
        print(self.Car_Load,'가(이) 차를 운전합니다')


'''
아빠차 = 자동차('아빠','black','gv80')
엄마차 = 자동차('엄마','red','g70')
내차 = 자동차('홍길동','white','k3')

아빠차.Car_Info()
엄마차.Car_Info()
내차.Car_Info()
'''
아빠차 = Car()
엄마차 = Car()
내차 = Car()

아빠차.Car_Info('아빠','black','gv80')
엄마차.Car_Info('엄마','red','g70')
내차.Car_Info('홍길동','white','k3')

엄마차.Car_Drive()