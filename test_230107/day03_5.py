<<<<<<< HEAD
chars = 'hello world, my name is python'
정수 = 314
실수 = 3.14
'''
for i in chars :
    print(i)

print()

i = 0
while i < len(chars) :
    print(chars[i], end = ' ')
    i += 1
'''
for i in range(len(chars)) :
    print(chars.count('o'),end=" ")


month = int(input('1~12월을 입력하세요>>'))

#1~12월 출력하되 입력받은 월은 skip
for i in range(12) :
    if i == month :
        break
    else :
        continue
    print((i+1),'월')

#1~12월 출력하되 입력받은 월부터는 출력안함
for i in range(month) :
    print((i+1),'월')
    if i == month :
        break

subway1 = 10
subway2 = 15
subway3 = 12
print()
list_subway = [10,15,12]
for i in list_subway : 
=======
chars = 'hello world, my name is python'
정수 = 314
실수 = 3.14
'''
for i in chars :
    print(i)

print()

i = 0
while i < len(chars) :
    print(chars[i], end = ' ')
    i += 1
'''
for i in range(len(chars)) :
    print(chars.count('o'),end=" ")


month = int(input('1~12월을 입력하세요>>'))

#1~12월 출력하되 입력받은 월은 skip
for i in range(12) :
    if i == month :
        break
    else :
        continue
    print((i+1),'월')

#1~12월 출력하되 입력받은 월부터는 출력안함
for i in range(month) :
    print((i+1),'월')
    if i == month :
        break

subway1 = 10
subway2 = 15
subway3 = 12
print()
list_subway = [10,15,12]
for i in list_subway : 
>>>>>>> 7dfafd19baae55259413a3bfdab76f37fce25b06
    print(i, '명')