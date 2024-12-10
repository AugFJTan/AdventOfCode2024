topology = []

with open('input.txt', 'r') as file:
    for line in file:
        topology.append(list(map(int, list(line.rstrip()))))

rows = len(topology)
cols = len(topology[0])

def adj(r, c):
    cells = []
    if r-1 >= 0:
        cells.append((r-1, c))
    if r+1 <= rows-1:
        cells.append((r+1, c))
    if c-1 >= 0:
        cells.append((r, c-1))
    if c+1 <= cols-1:
        cells.append((r, c+1))
    return cells

def count_trailheads(n, r, c, count, visited):
    if topology[r][c] == 9:
        if (r, c) not in visited:
            visited.append((r, c))
            count += 1
        return count

    cells = adj(r, c)

    for cell in cells:
        ar, ac = cell
        an = topology[ar][ac]
        if an != n + 1:
            continue
        count = count_trailheads(an, ar, ac, count, visited)

    return count

trailheads = 0

for r in range(rows):
    for c in range(cols):
        if topology[r][c] == 0:
            score = count_trailheads(0, r, c, 0, [])
            trailheads += score

print(trailheads)
