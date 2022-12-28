# req ANS:
# ['white', 'orange', 'red']
# ['black', 'yellow']

color_name1 = ["red", "orange", "green", "blue", "white"]
color_name2 = ["black", "yellow", "green", "blue"]
fnl_color1 = []
fnl_color2 = []
for i in color_name1:
    if i not in color_name2:
        fnl_color1.append(i)
for j in color_name2:
    if j not in color_name1:
        fnl_color2.append(j)

print(fnl_color1)
print(fnl_color2)