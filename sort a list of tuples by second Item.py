tup = [('for', 24), ('is', 10), ('Geeks', 28),
       ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]

lnt = len(tup)

for i in range(0, lnt):
    for j in range(0, lnt - i - 1):
        if (tup[j][1] > tup[j + 1][1]):
            temp = tup[j]
            tup[j] = tup[j + 1]
            tup[j + 1] = temp

print(tup)