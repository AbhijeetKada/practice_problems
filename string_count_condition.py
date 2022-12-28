i_p = ['abc', 'xyz', 'aba', '1221','afjhfa','rr']
count = 0
for i in i_p:
    if len(i) >=2:
        if i[0]==i[-1]:
            count+= 1
print(count)