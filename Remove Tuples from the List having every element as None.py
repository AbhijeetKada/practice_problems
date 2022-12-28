test_list = [(None, None), (None, None), (3, 4), (12, 3), (None,)]
res = []

for i in test_list:
    if i.count(None) != len(i):
        res.append(i)

print(res)