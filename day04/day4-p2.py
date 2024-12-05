word_matrix = []

with open('input.txt', 'r') as file:
    for line in file:
        word_matrix.append(list(line.rstrip()))

rows = len(word_matrix)
cols = len(word_matrix[0])

def xmax_count(r, c):
    bslash = word_matrix[r][c] + word_matrix[r+1][c+1] + word_matrix[r+2][c+2]
    fslash = word_matrix[r][c+2] + word_matrix[r+1][c+1] + word_matrix[r+2][c]
    return 1 if (bslash == 'MAS' or bslash == 'SAM') and (fslash == 'MAS' or fslash == 'SAM') else 0

total = 0

for r in range(rows-2):
    for c in range(cols-2):
        total += xmax_count(r, c)

print(total)
