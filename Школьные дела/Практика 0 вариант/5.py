def count_letters(word):
    letters = 'euoai'
    count = 0
    for c in letters:
        count += word.count(c)
    return count
def compare(s):
    return (len(s), -count_letters(s))

def sort_by(lst):
    return sorted(lst, key = compare)


n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print(*sort_by(strings), sep='\n')
