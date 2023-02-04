<<<<<<< HEAD
# 횟수를 입력받아서 그 수만큼 hello 출력하는 프로그램
'''
count = int(input('횟수를 입력하세요>>'))
i=0

while i < count :
    print((i+1),'번째 Hello')
    i += 1
'''

#1~100 사이에서 7의 배수만 출력하는 프로그램
'''
i = 1
while i < 101 :
    if i % 7 == 0 :
        print(i)
    i += 1
'''

# 금액은 얼마인가요?
'''
price = 300
money = int(input('금액은 얼마인가요>>'))
coffee = 0

while money >= price : 
    money -= price
    coffee += 1
    print('커피',coffee, '잔,','잔돈',money,'원')
'''
'''
변수1 = 123
변수2 = '문자열'
int(변수1)
print('안녕')
print(3.14)
print(변수2)
print('안녕 {}, {}'.format(변수2, 변수1))
print(f'안녕 {변수2},{변수1}')
'''

i = 3
if i == 3 :
    print('조건이 맞네요')
    print('조건이 맞으면 이 문장은 실행이 됩니다')
print('조건문이 끝났습니다')

i = 0
while i < 3 :
    print('반복문이 실행됩니다')
    print('조건이 맞는 동안에는 이 문장이 실행되겠네요',i)
    i += 1
=======
# 횟수를 입력받아서 그 수만큼 hello 출력하는 프로그램
'''
count = int(input('횟수를 입력하세요>>'))
i=0

while i < count :
    print((i+1),'번째 Hello')
    i += 1
'''

#1~100 사이에서 7의 배수만 출력하는 프로그램
'''
i = 1
while i < 101 :
    if i % 7 == 0 :
        print(i)
    i += 1
'''

# 금액은 얼마인가요?
'''
price = 300
money = int(input('금액은 얼마인가요>>'))
coffee = 0

while money >= price : 
    money -= price
    coffee += 1
    print('커피',coffee, '잔,','잔돈',money,'원')
'''
'''
변수1 = 123
변수2 = '문자열'
int(변수1)
print('안녕')
print(3.14)
print(변수2)
print('안녕 {}, {}'.format(변수2, 변수1))
print(f'안녕 {변수2},{변수1}')
'''

i = 3
if i == 3 :
    print('조건이 맞네요')
    print('조건이 맞으면 이 문장은 실행이 됩니다')
print('조건문이 끝났습니다')

i = 0
while i < 3 :
    print('반복문이 실행됩니다')
    print('조건이 맞는 동안에는 이 문장이 실행되겠네요',i)
    i += 1
>>>>>>> 7dfafd19baae55259413a3bfdab76f37fce25b06
print('반복문이 끝났습니다')