test_list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("enter number"))
    test_list.append(ele)

# l = [4, 10, 5, 3, 3]
i = int(input("enter 1 st index"))
j = int(input("enter 2 st index"))

ans = 0

for i in range(i, j + 1):
    ans += test_list[i]
print(ans)
