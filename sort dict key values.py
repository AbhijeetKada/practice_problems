test_dict = {'gfg': [7, 6, 3],
             'is': [2, 10, 3],
             'best': [19, 4]}

res = dict()
sor_dict = sorted(test_dict)

for key in sor_dict:
    res[key] = sorted(test_dict[key])


print( str(res))