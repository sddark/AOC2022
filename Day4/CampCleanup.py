import re

sections1 = open('real.txt', 'r').read().splitlines()
sections = []
score = 0
for x in sections1:
    sections.append(re.split(',|-',x))


print(sections)

for id in sections:

    if int(id[0]) >= int(id[2]) and int(id[0]) <= int(id[3]):
        score += 1
    elif int(id[1]) >= int(id[2]) and int(id[1]) <= int(id[3]):
        score += 1
    elif int(id[2]) >= int(id[0]) and int(id[2]) <= int(id[1]):
        score += 1
    elif int(id[3]) >= int(id[0]) and int(id[3]) <= int(id[1]):
        score += 1

print(score)