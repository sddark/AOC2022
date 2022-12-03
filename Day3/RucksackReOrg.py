import math
ruck = open('real.txt', 'r').read().splitlines()

print(ruck)
duplicates = []
for items in ruck:
    firstpart, secondpart = items[:len(items)//2], items[len(items)//2:]
    print(firstpart)
    print(secondpart)
    for x in firstpart:
        count = secondpart.count(x)
        if count >= 1:
            duplicates.append(x)
            break

print(duplicates)
score = 0
for dup in duplicates:
    if dup.islower():
        score += ord(dup) - 96
    else:
        score += ord(dup) - 38

print(score)