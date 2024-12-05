safe = 0

with open('input.txt', 'r') as file:
    for line in file:
        levels = list(map(int, line.rstrip().split()))
        is_safe = True
        trend = 0
        for i in range(len(levels)-1):
            delta = levels[i+1] - levels[i]
            if delta == 0 or abs(delta) > 3:
                is_safe = False
            elif trend == 0:
                if delta < 0:
                    trend = -1
                else:
                    trend = 1
                continue
            elif trend == -1 and delta > 0:
                is_safe = False
            elif trend == 1 and delta < 0:
                is_safe = False
        if is_safe:
            safe += 1

print(safe)
