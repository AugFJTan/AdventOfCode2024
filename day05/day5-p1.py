rules = []

rules_end = False

total = 0

with open('input.txt', 'r') as file:
    for line in file:
        data = line.rstrip()
        if data == '':
            rules_end = True
            continue
        if not rules_end:
            lhs, rhs = data.split('|')
            rules.append((int(lhs), int(rhs)))
        else:
            pages = list(map(int, data.split(',')))
            passing = True
            for rule in rules:
                lhs, rhs = rule
                if lhs in pages and rhs in pages:
                    if pages.index(lhs) > pages.index(rhs):
                        passing = False
            if passing:
                total += pages[len(pages)//2]

print(total)
