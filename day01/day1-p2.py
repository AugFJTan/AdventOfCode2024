llist = []
rlist = []

with open('input.txt', 'r') as file:
    for line in file:
        lhs, rhs = line.rstrip().split()
        llist.append(int(lhs))
        rlist.append(int(rhs))

total = 0

for i in range(len(llist)):
    total += llist[i] * rlist.count(llist[i])

print(total)
