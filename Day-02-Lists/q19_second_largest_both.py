l_num=[10, 45, 72, 90, 55]
l_num.sort()
print("The second largest number is :",l_num[-2])

print("Without Sort")

l_num = [5, 5, 5, 10]

largest = l_num[0]
second = l_num[0]

for i in l_num:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Largest:", largest)
print("Second Largest:", second)
