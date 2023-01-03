from collections import defaultdict

test_list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter number"))
    test_list.append(ele)
#test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]

res = defaultdict(list)
for ele in test_list:
    res[ele].append(ele)

val = str(dict(res))
print(val)