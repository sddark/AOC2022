cals = open('real.txt', 'r').read().splitlines()
total_cals = 0
max_cals = 0
for x in cals:
    if len(x) == 0: 
        if total_cals > max_cals:
            max_cals = total_cals
        total_cals = 0
    else:
        total_cals += int(x)

print(max_cals)
