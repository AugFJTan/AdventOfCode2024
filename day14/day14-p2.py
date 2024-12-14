from PIL import Image

rows = 103
cols = 101

bathroom = []
robots = []

for _ in range(rows):
    bathroom.append([0] * cols)

with open('input.txt', 'r') as file:
    for line in file:
        pos, vel = line.rstrip().split()
        px, py = list(map(int, pos[2:].split(',')))
        vx, vy = list(map(int, vel[2:].split(',')))
        bathroom[py][px] += 1
        robots.append([px, py, vx, vy])

def move_robots():
    for i in range(len(robots)):
        px, py, vx, vy = robots[i]

        bathroom[py][px] -= 1

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

        robots[i][0] = px
        robots[i][1] = py

seconds = 1

for _ in range(10403):
    move_robots()

    image = Image.new('RGB', (cols, rows), (0xff, 0xff, 0xff))

    for r in range(rows):
        for c in range(cols):
            if bathroom[r][c] > 0:
                image.putpixel((c, r), (0xff, 0x00, 0x00))

    image.save(f'output/s-{seconds:03d}.png')

    seconds += 1
