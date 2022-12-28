list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

res1 = []
res2 = []

for i in list1:
    if i not in list2:
        res1.append(i)
print("missing in list2:",res1)
for i in list2:
    if i not in list1:
        res2.append(i)
print("missing in list1:",res2)