my_list = []
n = int(input("Enter number of elements : "))
v = int(input("Enter number to check index: "))
for i in range(0, n):
    ele = int(input("enter number"))
    my_list.append(ele)

# my_list = [1, 2, 3, 1, 5, 4]

list_size = len(my_list)

for itr in range(list_size):
    if (my_list[itr] == v):
        print(itr)
