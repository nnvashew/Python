n = int(input())
numbers = []
result = []
summ = 0
for i in range(n):
    numbers.append(int(input()))
    summ+=numbers[i]
for num in numbers:
    if num % 2 == summ % 2:
        result.append(num)
print(summ-sum(result), result)