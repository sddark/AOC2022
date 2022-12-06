message = open('real.txt', 'r').read()
print(message)
packet = set()
for j in range(0, len(message)-14):
    packet.clear()
    for i in range(j, j+14):
        packet.add(message[i])
    if len(packet) > 13:
        print(j+14)
        break

""" print(len(packet))
print(len(message))
print(packet) """