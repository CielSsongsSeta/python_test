# 기타 제어문

for i in range(10) :
    print((i+1),'번째 hello')
    if i == 2 :
        break

for i in range(10) :
    if i >= 3 and i < 7 :
        continue
    print((i+1),'번째 bye')