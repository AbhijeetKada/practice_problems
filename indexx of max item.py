
list1 = [ 2, 4, 6, 1, 8, 5, 3 ]
ind = 0
max_element = list1[0]

for i in range (1,len(list1)):
    if list1[i] > max_element:
        max_element = list1[i]
        ind = i

print(ind)
