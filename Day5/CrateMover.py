import re

stack1 = ['W', 'B', 'D', 'N', 'C', 'F', 'J']
stack2 = ['P', 'Z', 'V', 'Q', 'L', 'S', 'T']
stack3 = ['P', 'Z', 'B', 'G', 'J', 'T']
stack4 = ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C']
stack5 = ['G', 'V', 'B', 'J', 'S']
stack6 = ['P', 'S', 'Q']
stack7 = ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N']
stack8 = ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R']
stack9 = ['V', 'D', 'T', 'R']

temp_stack = []

stacking = open('real.txt', 'r').read().splitlines()
print(stacking)
moving_crates = []
for x in stacking:
    moving_crates.append(re.split('move | from | to ',x))

for i in moving_crates:
    if int(i[2]) == 1:
        for j in range(0, int(i[1])):
            a = stack1.pop()
            temp_stack.append(a)
    elif int(i[2]) == 2:
        for j in range(0, int(i[1])):
            a = stack2.pop()
            temp_stack.append(a)
    elif int(i[2]) == 3:
        for j in range(0, int(i[1])):
            a = stack3.pop()
            temp_stack.append(a)
    elif int(i[2]) == 4:
        for j in range(0, int(i[1])):
            a = stack4.pop()
            temp_stack.append(a)
    elif int(i[2]) == 5:
        for j in range(0, int(i[1])):
            a = stack5.pop()
            temp_stack.append(a)
    elif int(i[2]) == 6:
        for j in range(0, int(i[1])):
            a = stack6.pop()
            temp_stack.append(a)
    elif int(i[2]) == 7:
        for j in range(0, int(i[1])):
            a = stack7.pop()
            temp_stack.append(a)
    elif int(i[2]) == 8:
        for j in range(0, int(i[1])):
            a = stack8.pop()
            temp_stack.append(a)
    else:
        for j in range(0, int(i[1])):
            a = stack9.pop()
            temp_stack.append(a)            
    

    if int(i[3]) == 1:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack1.append(a)
    elif int(i[3]) == 2:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack2.append(a)
    elif int(i[3]) == 3:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack3.append(a)
    elif int(i[3]) == 4:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack4.append(a)
    elif int(i[3]) == 5:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack5.append(a)
    elif int(i[3]) == 6:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack6.append(a)
    elif int(i[3]) == 7:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack7.append(a)
    elif int(i[3]) == 8:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack8.append(a)
    else:
        for j in range(0, int(i[1])):
            a = temp_stack.pop()
            stack9.append(a)
    


print(stack1)
print(stack2)
print(stack3)
print(stack4)
print(stack5)
print(stack6)
print(stack7)
print(stack8)
print(stack9)


'''
FIFO operation
a = stack2.pop()
stack2.append(a)
'''

