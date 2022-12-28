list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

dup = []
lt = len(list1)
for i in range(lt):
    k = i + 1
    for j in range(k, lt):
        if list1[i] == list1[j] and list1[i] not in dup:
            dup.append(list1[i])

print(dup)
