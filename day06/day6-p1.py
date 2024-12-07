patrol_map = []

with open('input.txt', 'r') as file:
    for line in file:
        patrol_map.append(list(line.rstrip()))

rows = len(patrol_map)
cols = len(patrol_map[0])

start_pos = None

for r in range(rows):
    for c in range(cols):
        if patrol_map[r][c] == '^':
            start_pos = (r, c)
            patrol_map[r][c] = 'X'
            break

UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

direction = UP
current_pos = start_pos

def in_map(r, c):
    return (r >= 0 and r <= rows-1) and \
           (c >= 0 and c <= cols-1)

while True:
    r, c = current_pos

    if direction == UP:
        nr, nc = r-1, c
    elif direction == RIGHT:
        nr, nc = r, c+1
    elif direction == DOWN:
        nr, nc = r+1, c
    else: # direction == LEFT:
        nr, nc = r, c-1
    
    if not in_map(nr, nc):
        break
    
    if patrol_map[nr][nc] == '#':
        if direction == UP:
            direction = RIGHT
        elif direction == RIGHT:
            direction = DOWN
        elif direction == DOWN:
            direction = LEFT
        else: # direction == LEFT
            direction = UP
    else:
        current_pos = (nr, nc)
        patrol_map[nr][nc] = 'X'

count = 0

for r in range(rows):
    for c in range(cols):
        if patrol_map[r][c] == 'X':
            count += 1

print(count)
