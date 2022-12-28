test_tup = (5, 20, 3, 7, 6, 8)
k = 2
sort_tup = sorted(test_tup)
list_tup = list(sort_tup)
lent = len(sort_tup)
res = []
for idx, i in enumerate(list_tup):
    if idx < k or idx >= lent - k:
        res.append(i)
print(str(res))
