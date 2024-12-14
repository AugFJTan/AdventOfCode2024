rows = 103
cols = 101

bathroom = []

for _ in range(rows):
    bathroom.append([0] * cols)

with open('input.txt', 'r') as file:
    for line in file:
        pos, vel = line.rstrip().split()
        px, py = list(map(int, pos[2:].split(',')))
        vx, vy = list(map(int, vel[2:].split(',')))
        
        for _ in range(100):
            px += vx
            py += vy
            
            if px < 0:
                px = cols - abs(px)
            elif px > cols - 1:
                px = px - cols

            if py < 0:
                py = rows - abs(py)
            elif py > rows - 1:
                py = py - rows
            
        bathroom[py][px] += 1

def safety_factor(ar, ac, br, bc):
    score = 0
    for r in range(ar, br):
        for c in range(ac, bc):
            score += bathroom[r][c]
    return score

mr = rows // 2
mc = cols // 2

score  = safety_factor(0, 0, mr, mc)
score *= safety_factor(0, mc+1, mr, cols)
score *= safety_factor(mr+1, 0, rows, mc)
score *= safety_factor(mr+1, mc+1, rows, cols)

print(score)
