my_list = [12,35,67,35,78,53,78,97]
first = my_list[-1]
last = my_list[0]
my_list.pop(0)
my_list.pop(-1)
my_list.insert(0,first)
my_list.append(last)
print(my_list)