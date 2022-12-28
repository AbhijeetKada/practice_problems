test_tup =([5, 6], [6, 7, 8, 9], [3])

res = []

for i in test_tup:
    for j in i:
        if j not in res:
            res.append(j)
print(tuple(res))