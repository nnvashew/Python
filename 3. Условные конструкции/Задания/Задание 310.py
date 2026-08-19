n = int(input())
if n%4==0 or n%400==0:
    print('YES')
if n%100==0:
    print('NO')