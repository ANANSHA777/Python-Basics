l_num = [10, 20, 10, 30, 20, 40]
new_list=[]
for i in l_num:
    if i not in new_list:
        new_list.append(i)

print("New List is",new_list)
