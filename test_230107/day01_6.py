#이름 = input("이름은 무엇인가요? : ")
#나이 = int(input("나이는 몇살인가요? : "))
#성별 = input('성별은 무엇인가요? : ')
#키 = float(input("키는 몇인가요? : "))
#
#print()
#print('안녕하세요 제 이름은 '+ 이름 +'입니다.')
#print('나이는 ', 나이 ,'살이고 성별은 '+ 성별 +'입니다.')
#print('키는 ', 키 , 'cm입니다.')

# 10~99 사이의 숫자를 입력받아서 십의자리와 일의자리를 알려주기

print()
number_input = int(input("10~99 사이의 숫자를 입력하세요 : "))

print()
print("십의 자리 : ",int(number_input/10))
print("일의 자리 : ",int(number_input%10))