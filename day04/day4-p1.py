word_matrix = []

with open('input.txt', 'r') as file:
    for line in file:
        word_matrix.append(list(line.rstrip()))

rows = len(word_matrix)
cols = len(word_matrix[0])

def xmax_count(a, b, c, d):
    ar, ac = a
    br, bc = b
    cr, cc = c
    dr, dc = d
    word  = word_matrix[ar][ac] + word_matrix[br][bc] + word_matrix[cr][cc] + word_matrix[dr][dc]
    return 1 if word == 'XMAS' else 0

total = 0

# East
for r in range(rows):
    for c in range(cols-3):
        total += xmax_count((r,c), (r,c+1), (r,c+2), (r,c+3))

# West
for r in range(rows):
    for c in range(3, cols):
        total += xmax_count((r,c), (r,c-1), (r,c-2), (r,c-3))

# South
for r in range(rows-3):
    for c in range(cols):
        total += xmax_count((r,c), (r+1,c), (r+2,c), (r+3,c))

# North
for r in range(3, rows):
    for c in range(cols):
        total += xmax_count((r,c), (r-1,c), (r-2,c), (r-3,c))

# Southeast
for r in range(rows-3):
    for c in range(cols-3):
        total += xmax_count((r,c), (r+1,c+1), (r+2,c+2), (r+3,c+3))

# Northwest
for r in range(3, rows):
    for c in range(3, cols):
        total += xmax_count((r,c), (r-1,c-1), (r-2,c-2), (r-3,c-3))

# Southwest
for r in range(rows-3):
    for c in range(3, cols):
        total += xmax_count((r,c), (r+1,c-1), (r+2,c-2), (r+3,c-3))

# Northeast
for r in range(3, rows):
    for c in range(cols-3):
        total += xmax_count((r,c), (r-1,c+1), (r-2,c+2), (r-3,c+3))

print(total)
