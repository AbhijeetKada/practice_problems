test_dict = {'gfg': {'Manjeet': 5, 'Himani': 10},
             'is': {'Manjeet': 8, 'Himani': 9},
             'best': {'Manjeet': 10, 'Himani': 15}}

key = 'Himani'

res = None
res_max = 0
for sub in test_dict:
    if test_dict[sub][key] > res_max:
        res_max = test_dict[sub][key]
        res = sub

print(str(res))
