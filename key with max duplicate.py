
test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}
max_val = 0
max_key = None
for sub in test_dict:
    val = set(test_dict[sub])
    lnt = len(val)
    if lnt > max_val:
        max_val = lnt
        max_key = sub


print(str(max_key))
