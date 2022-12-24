numbers = [2, 3, 2, 2, 2, 4, 5, 6, 6, 3, 3]
newitem = []
for number in numbers:
    if number not in newitem:
        newitem.append(number)
print(newitem)