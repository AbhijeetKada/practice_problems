test_str = "gfg is best for all geeks"

sub_list = ["best", "all"]
b = test_str.split()
x = []
for i in b:
    if i not in sub_list:
        x.append(i)
res = " ".join(x)

print(res)
