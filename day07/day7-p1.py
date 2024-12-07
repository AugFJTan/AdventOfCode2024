def operate(nums, result, test):
    if nums == []:
        return result == test

    a = operate(nums[1:], result + nums[0], test)
    b = operate(nums[1:], result * nums[0], test)

    return a or b

total = 0

with open('input.txt', 'r') as file:
    for line in file:
        test, nums = line.split(':')
        test = int(test)
        nums = list(map(int, nums.split()))
        if operate(nums[1:], nums[0], test):
            total += test

print(total)
