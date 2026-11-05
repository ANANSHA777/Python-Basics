l_num=[10, 20, 30, 40, 50] 
found=False
num=int(input("Enter a Number :"))
for i in l_num:
    if i==num:
        found=True
        break
if found==True:
    print("Number Found in list")
else:
    print("Number Not Found in list")
