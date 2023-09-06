numbers = [1, 5, 3, 7]
for i in range (len(numbers)-1):
    for j in range (len(numbers)-i-1):
        if numbers[j] < numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)