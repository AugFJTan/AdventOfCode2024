initial_state = "9759 0 256219 60 1175776 113 6 92833"

data = initial_state.split()

for _ in range(25):
    for i in range(len(data)):
        if data[i] == '0':
            data[i] = '1'
        elif len(data[i]) % 2 == 0:
            mid = len(data[i]) // 2
            lhs = str(int(data[i][:mid]))
            rhs = str(int(data[i][mid:]))
            data[i] = [lhs, rhs]
        else:
            data[i] = str(int(data[i]) * 2024)

    new_data = []

    for i in range(len(data)):
        if isinstance(data[i], list):
            new_data.append(data[i][0])
            new_data.append(data[i][1])
        else:
            new_data.append(data[i])

    data = new_data

print(len(data))
