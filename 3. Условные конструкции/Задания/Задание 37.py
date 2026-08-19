n = int(input())
if n%10>1 and n%10<5 and (n%100<10 or n%100>14):
    print('гриба')
elif n%10 == 1 and n%100!=11:
    print('гриб')
else:
    print('грибов')