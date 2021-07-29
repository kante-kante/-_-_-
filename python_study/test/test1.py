a = int(input("원하는 a 값을 입력하시오: "))
b = int(input("원하는 b 값을 입력하시오: "))
y = a * b

if y > 0:
    y = y - 1
    y = y / 2
else :
    y = y + 10
    y = y / 2

print(y)

'''elif y > 0:
    y = y + 10
if y > 0:
    y = y / 2
else:
    y = y * 2'''


'''elif y > 0:
    y = y / 2
else:
    y = y * 2'''