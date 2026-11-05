l_num=[10, 20, 10, 30, 10, 40] 
count=0
num=int(input("Enter a Number :"))
for i in l_num:
    if i==num:
        count = count + 1
print("Number",num,"Occurs",count,"times")
