test_dict = {'gfg': 4, 'is': 2, 'best': 5}
lt_dict = list(test_dict.items())
rev_dict = reversed(lt_dict)
res = dict(rev_dict)

print( str(res))