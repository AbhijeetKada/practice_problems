test_list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter number"))
    test_list.append(ele)

#test_list = [12, 67, 98, 34]

res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)

print( str(res))
