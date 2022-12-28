test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
lent = len(test_list)
res = []
count = 0
for i in test_list:

    lnt = len(i)

    for j in i:
        if j > 0:
            count += 1
    if count == lnt:
        res.append(i)

print(res)