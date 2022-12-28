str_input = 'lkseropewdssafsdfafkpwe'

final = {}
f_t = []
fin = []
finl = []
for i in str_input:
    if i in final:
        final[i] = final[i] + 1
    else:
        final[i] = 1

lt_tp = list(final.items())

max_val = max(lt_tp, key=lambda x:x[1])
for i in lt_tp:
    if i != max_val:
      f_t.append(i)
max_val1 = max(f_t, key=lambda y:y[1])
for i in f_t:
    if i[-1]==max_val1[-1]:
        fin.append(i)
finl.append(max_val)
finl.append(fin)
print(finl)
