import re

total = 0

with open('input.txt', 'r') as file:
    for line in file:
        instructions = re.findall(r'mul\((\d+),(\d+)\)', line)
        for inst in instructions:
            x, y = inst
            total += int(x) * int(y)

print(total)
