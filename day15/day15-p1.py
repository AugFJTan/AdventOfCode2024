warehouse = []
movement = []

map_end = False

with open('input.txt', 'r') as file:
    for line in file:
        data = line.rstrip()
        if data == '':
            map_end = True
            continue
        if not map_end:
            warehouse.append(list(data))
        else:
            movement.extend(list(data))

rows = len(warehouse)
cols = len(warehouse[0])

robot_r = None
robot_c = None

for r in range(rows):
    for c in range(cols):
        if warehouse[r][c] == '@':
            robot_r = r
            robot_c = c
            warehouse[r][c] = '.'
            break

def move_boxes(r, c, dr, dc):
    if warehouse[r+dr][c+dc] == '#':
        return [False, 0, 0]
    elif warehouse[r+dr][c+dc] == '.':
        return [True, r+dr, c+dc]
    else: # warehouse[r+dr][c+dc] == 'O'
        return move_boxes(r+dr, c+dc, dr, dc)

for move in movement:
    r = robot_r
    c = robot_c
    dr = 0
    dc = 0

    if move == '^':
        dr = -1
    elif move == 'v':
        dr = 1
    elif move == '<':
        dc = -1
    else: # move == '>'
        dc = 1

    nr = r+dr
    nc = c+dc

    if warehouse[nr][nc] == '#':
        continue
    elif warehouse[nr][nc] == '.':
        robot_r = nr
        robot_c = nc
    else: # warehouse[nr][nc] == 'O'
        success, fr, fc = move_boxes(nr, nc, dr, dc)
        if success:
            warehouse[nr][nc] = '.'
            warehouse[fr][fc] = 'O'
            robot_r = nr
            robot_c = nc

total = 0

for r in range(1, rows-1):
    for c in range(1, cols-1):
        if warehouse[r][c] == 'O':
            total += r * 100 + c

print(total)
