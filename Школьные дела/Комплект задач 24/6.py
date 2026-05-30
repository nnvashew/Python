n=int(input())
s=set()
for i in range(n):
   s = s.union(set(input()))
print(len(s))