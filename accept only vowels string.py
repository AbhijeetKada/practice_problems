str_value = str(input("enter the string"))
new_list = [char for char in str_value.lower() if char in 'aeiou']

if new_list:
    dic = {}
    lst = []

    for char in new_list:
        dic['a'] = new_list.count('a')
        dic['e'] = new_list.count('e')
        dic['i'] = new_list.count('i')
        dic['o'] = new_list.count('o')
        dic['u'] = new_list.count('u')

    for i, j in dic.items():
        if j == 0:
            lst.append(i)

    if lst:
        print("All vowels except {','.join(lst)} are not present")
    else:
        print('All vowels are present')
else:
    print("No vowels present")
