test_tuple1 = (7, 2, 5)
test_tuple2 = (7, 8, 4)
res = []

for i in test_tuple1:
    for j in test_tuple2:
        res.append((i,j))

for k in test_tuple2:
    for l in test_tuple1:
        res.append((k,l))

print(res)