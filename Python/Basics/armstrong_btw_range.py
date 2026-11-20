st = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))

for i in range(st, end+1):
    sum = 0
    count = 0
    temp = i
    original = i

    if i == 0:
        count = 1
    else:
        while temp > 0:
            digit = temp % 10
            temp //= 10
            count += 1

    while original > 0:
        dig = original % 10
        original //= 10
        sum = sum + dig ** count

    if sum == i:
        print(i)
        

