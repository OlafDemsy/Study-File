number = [1, 4, 5, 6, 23, 24]
max = number[0]
for numbers in number:
    if max < numbers:
        max = numbers
print(max)
