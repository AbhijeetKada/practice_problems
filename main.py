my_list = [[1], [2, 3], [4, 5, 6, 7]]
str_list = []
digit_list = []
final_list = []
for i in my_list:
    for j in i:
        str_list.append(str(j)* j)
int_list= map(int, str_list)
for i in int_list:
    digit_list.append([int(x) for x in str(i)])
for j in digit_list:
    for k in j:
        final_list.append(k)
print(final_list)