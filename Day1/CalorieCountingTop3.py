cals = open('real.txt', 'r').read().splitlines()
cals.append('')
total_cals = 0
max_cals = [0, 0, 0]
print(cals)
for x in cals:
    if len(x) == 0: 
        if total_cals > max_cals[0]:
            max_cals.insert(0, int(total_cals))
            max_cals.pop(3)
        elif total_cals > max_cals[1]:
            max_cals.insert(1, int(total_cals))
            max_cals.pop(3)
        elif total_cals > max_cals[2]:
            max_cals.insert(2, int(total_cals))
            max_cals.pop(3)
        total_cals = 0
    else:
        total_cals += int(x)

print(max_cals)
sum_top_three = 0
for x in max_cals:
    sum_top_three += x

print(sum_top_three)