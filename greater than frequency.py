test_list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter number"))
    test_list.append(ele)

#test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

K = 2

res = []
for i in test_list:
    freq = test_list.count(i)

    if freq > K and i not in res:
        res.append(i)

print(str(res))
