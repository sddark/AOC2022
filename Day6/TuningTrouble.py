message = open('test.txt', 'r').read()
print(message)
packet = set()
for j in range(0, len(message)-4):
    packet.clear()
    for i in range(j, j+4):
        packet.add(message[i])
    if len(packet) > 3:
        print(j+4)
        break

""" print(len(packet))
print(len(message))
print(packet) """