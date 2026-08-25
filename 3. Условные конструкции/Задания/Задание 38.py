a = int(input())
b = int(input())
c = int(input())
if b < a:
    a, b = b, a
if b > c:
    b, c = c, b
if b < a:
    a, b = b, a

print(a, b, c)