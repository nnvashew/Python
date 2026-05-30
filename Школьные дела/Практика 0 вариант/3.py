def zamena(line):
    for l in 'qwertyuiopasdfghjklzxcvbnm':
        line = line.replace(l, l.upper())
    return line

line = input()
print(zamena(line))