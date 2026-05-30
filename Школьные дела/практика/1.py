n = int(input())
people = []
for i in range(n):
    people.append(input().split())
people.sort(key=lambda s: (s[0], s[1]))
print(*people)