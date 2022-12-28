#REQ ANS ::: ['Green', 'White', 'Black']

i_p =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

indx = [0,4,5]
fnl = []
for i in i_p:
    if i_p.index(i) not in indx:
        fnl.append(i)
print(fnl)