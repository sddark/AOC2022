import math
ruck = open('real.txt', 'r').read().splitlines()

print(ruck)
one_third = math.floor(len(ruck)/3)
print(one_third)
duplicates = []
for i in range(0,one_third):
    for item in ruck[i*3]:
        if item in ruck[i*3 + 1] and item in ruck[i*3 + 2]:
            duplicates.append(item)
            break

print(duplicates)
score = 0
for dup in duplicates:
    if dup.islower():
        score += ord(dup) - 96
    else:
        score += ord(dup) - 38

print(score)