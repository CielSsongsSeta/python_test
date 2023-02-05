'''
자료형 : str, int, float, list, dict, set, tuple,...
str - 문자열
int - 정수형
float - 실수형
list - 리스트
dict - 딕셔너리

연산자 : 특정 기능을 갖고 있는 기호
+ - * / % ** //

누적연산자 : 연산 후 그 값을 다시 대입
+= -= *= /= %=

관계연산자 : and, or, not
비교연산자 : > < <= >= == !=

제어문
- 조건문 : if~elif~else
- 반복문 : while, for
- 기타제어문 : break, continue

함수 : 코드를 저장하는 기술, 코드 변화 대처에 용이(코드 재활용)
- 내장함수 : python에서 지원해주는 함수
- 외장함수 : python에서 제공해주지 않으나 import로 추가한 함수
- 사용자 정의 함수 : 내가 직접 만드는 연산자 def

외부모듈 추가
pip~~
import 모듈명
import 모듈명 as 별명
from 모듈명 import 모듈일부

클래스 : 변수와 함수를 묶는 기술(가독성을 위해서)
    멤버변수 - 클래스 안에서 생성한 변수(self. 을 통해서 사용 가능)
    메서드 - 클래스 안에서 정의된 함수(self를 갖고 있음)

    객체화 - 클래스를 사용하기 위해서는 변수에 담아 사용한다. 이때 변수는 객체라고 부른다.
    생성자 - 객체화하는 순간에 사용되는 메서드 def __init__(self): 
    상속 - 클래스를 복붙, 복붙한 다음에 메서드를 추가하거나 재정의
'''

class MyClass:
    멤버변수1 = ''
    멤버변수2 = 0
    멤버변수3 = []
    def 메서드1(self):
        print('메서드1 사용')
    def 메서드2(self, str1, num1):
        self.멤버변수1 = str1
        self.멤버변수2 = num1
        self.멤버변수3.append(str1)
        self.멤버변수3.append(num1)
    def __init__(self):
        self.메서드1()

객체변수=MyClass()
객체변수.메서드2('sample',1)

class MyClassEx(MyClass): # 상속 : ()에 있는 클래스를 내 클래스에 복붙한다.
    pass