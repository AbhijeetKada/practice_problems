
test_list = [{"Gfg": {"a": 5, "b": 8, "c": 9}},
             {"is": {"f": 8, "j": 8, "k": 10}},
             {"Best": {"i": 16}}]


K = 8

res = list()

for sub in test_list:
    for key, val in sub.items():
        for key1, val1 in val.items():
            if val1 != K:
                res.append({key1: val1})

print(str(res))
