a = int(input())
b = int(input())
c = int(input())
h = max(a,b,c)
k1 = min(a,b,c)
k2 = a+b+c-k1-h
if k1+k2<=h:
    print('Не существует')
if k1**2+k2**2==h**2:
    print('Прямоугольный')
if k1**2+k2**2>h**2:
    print('Остроугольный')
if k1**2+k2**2<h**2:
    print('Тупоугольный')