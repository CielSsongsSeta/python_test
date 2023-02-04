<<<<<<< HEAD
def 더하기 (num1, num2, num3):
    print(num1+num2+num3)

def 빼기곱하기나누기 (num1, num2, num3):
    print(num1-num2-num3)
    print(num1*num2*num3)
    print(num1/num2/num3)

def 빼기 (num1, num2, num3):
    print(num1-num2-num3)

def 곱하기 (num1, num2, num3):
    print(num1*num2*num3)

def 나누기 (num1, num2, num3):
    print(num1/num2/num3)

print(1+2)
더하기(1,2,3)
빼기(3,2,1)
곱하기(1,2,3)
나누기(10,2,2)

def 거리계산(num1,num2):
    if num1 < 0 :
        num1*= -1
    if num2 < 0 :
        num2*= -1
    #print(num1+num2)
    return num1+num2 

결과1 = 거리계산(3,7)
결과2 = 거리계산(-4,3)
print(결과2)

lst = [10,20,30,40,50]

def 총합(a_lst):
    number = 0
    for i in range(len(a_lst)):
        number += a_lst[i]
    return number

sum = 총합(lst)
avg = sum/len(lst)

print('총합은', sum)
print('평균은', avg)

def star():
    num_a = int(input("별의 개수를 입력하세요 : "))
    for i in range(num_a):
        print("*", end="")
    print("")

=======
def 더하기 (num1, num2, num3):
    print(num1+num2+num3)

def 빼기곱하기나누기 (num1, num2, num3):
    print(num1-num2-num3)
    print(num1*num2*num3)
    print(num1/num2/num3)

def 빼기 (num1, num2, num3):
    print(num1-num2-num3)

def 곱하기 (num1, num2, num3):
    print(num1*num2*num3)

def 나누기 (num1, num2, num3):
    print(num1/num2/num3)

print(1+2)
더하기(1,2,3)
빼기(3,2,1)
곱하기(1,2,3)
나누기(10,2,2)

def 거리계산(num1,num2):
    if num1 < 0 :
        num1*= -1
    if num2 < 0 :
        num2*= -1
    #print(num1+num2)
    return num1+num2 

결과1 = 거리계산(3,7)
결과2 = 거리계산(-4,3)
print(결과2)

lst = [10,20,30,40,50]

def 총합(a_lst):
    number = 0
    for i in range(len(a_lst)):
        number += a_lst[i]
    return number

sum = 총합(lst)
avg = sum/len(lst)

print('총합은', sum)
print('평균은', avg)

def star():
    num_a = int(input("별의 개수를 입력하세요 : "))
    for i in range(num_a):
        print("*", end="")
    print("")

>>>>>>> 7dfafd19baae55259413a3bfdab76f37fce25b06
star()