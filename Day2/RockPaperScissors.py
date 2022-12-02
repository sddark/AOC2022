rounds = open('real.txt', 'r')
score = 0

for i in rounds:
    if i[2] == 'X':
        score += 1
        if i[0] == 'A':
            score += 3
        elif i[0] == 'B':
            pass
        else:
            score += 6
    elif i[2] == 'Y':
        score += 2
        if i[0] == 'A':
            score += 6
        elif i[0] == 'B':
            score += 3
        else:
            pass
    else:
        score += 3
        if i[0] == 'A':
            pass
        elif i[0] == 'B':
            score += 6
        else:
            score += 3

    print(score)

print(score)