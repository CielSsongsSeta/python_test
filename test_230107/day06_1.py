<<<<<<< HEAD
변수 = '저장공간(문자열형)'
정수형 = 314
실수형 = 3.14

변수 = '문자열형'

print(정수형)
print(실수형)
print(변수)
print('내가 저장한 값 :',변수,',',실수형)
print('내가 저장한 값 :{},{}'.format(변수,실수형))
print(f'내가 저장한 값:{변수},{실수형}')

lst = [1,2,3,'hello',4,5,6]
tup = (1,2,3,'hello',4,5,6)
s ={1,2,3,'hello',4,5,6}
dic = {'A':'에이','B':'비','C':'씨',1:1.0}

lst.append('맨 뒤에 추가')
print(lst)
lst.pop()
print(lst)

for item in lst :
    print(item, end = ' ')
print()

dic['추가할 키워드'] = '추가할 값'
dic[1] = '일'
print(dic)

print(lst[0])
print(dic['A'])

for i in dic :
    print(dic[i], end=' ')
    print(dic.get(i), end = ' ')

변수 = input('입력할 문자열을 알려주세요>>')
정수형 = int(input('입력할 정수를 알려주세요>>'))
print('내가 입력한 문자열 :',변수,'\n내가 입력한 정수형 :',정수형)

if 정수형 < 10 :
    print('10보다 작네요')
elif 정수형 < 100 :
    print('100보다 작네요')
else :
    print('100 이상')

for i in range(5) :
    print('5번 반복',i)

for i in lst :
    if i == 'hello' :
        print('hello 찾음')
=======
변수 = '저장공간(문자열형)'
정수형 = 314
실수형 = 3.14

변수 = '문자열형'

print(정수형)
print(실수형)
print(변수)
print('내가 저장한 값 :',변수,',',실수형)
print('내가 저장한 값 :{},{}'.format(변수,실수형))
print(f'내가 저장한 값:{변수},{실수형}')

lst = [1,2,3,'hello',4,5,6]
tup = (1,2,3,'hello',4,5,6)
s ={1,2,3,'hello',4,5,6}
dic = {'A':'에이','B':'비','C':'씨',1:1.0}

lst.append('맨 뒤에 추가')
print(lst)
lst.pop()
print(lst)

for item in lst :
    print(item, end = ' ')
print()

dic['추가할 키워드'] = '추가할 값'
dic[1] = '일'
print(dic)

print(lst[0])
print(dic['A'])

for i in dic :
    print(dic[i], end=' ')
    print(dic.get(i), end = ' ')

변수 = input('입력할 문자열을 알려주세요>>')
정수형 = int(input('입력할 정수를 알려주세요>>'))
print('내가 입력한 문자열 :',변수,'\n내가 입력한 정수형 :',정수형)

if 정수형 < 10 :
    print('10보다 작네요')
elif 정수형 < 100 :
    print('100보다 작네요')
else :
    print('100 이상')

for i in range(5) :
    print('5번 반복',i)

for i in lst :
    if i == 'hello' :
        print('hello 찾음')
>>>>>>> 7dfafd19baae55259413a3bfdab76f37fce25b06
        break