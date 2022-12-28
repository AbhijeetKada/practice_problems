test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

lt = list(test_tup)
res = []

for i in lt:
    if i not in res:
        res.append(i)

print(res)
