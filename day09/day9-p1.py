disk = []

with open('input.txt', 'r') as file:
    data = file.read().rstrip()
    for i in range(len(data)):
        if i % 2 == 0:
            disk += [i // 2] * int(data[i])
        else:
            disk += [-1] * int(data[i])

lidx = disk.index(-1)
ridx = len(disk)-1

while lidx != ridx+1:
    if disk[ridx] != -1:
        disk[lidx] = disk[ridx]
        disk[ridx] = -1
    lidx = disk.index(-1)
    ridx -= 1

checksum = 0

for i in range(len(disk)):
    if disk[i] == -1:
        break
    checksum += i * disk[i]

print(checksum)
