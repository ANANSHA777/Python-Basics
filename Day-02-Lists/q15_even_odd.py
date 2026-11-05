l_num=[10, 77, 45, 72, 65, 90, 55, 33, 82] 
even = 0
odd = 0
for i in l_num:
    if i %2==0:
        even = even+1
    else:
        odd= odd+1
print("Even number count = ",even)
print("Odd number count = ",odd)
