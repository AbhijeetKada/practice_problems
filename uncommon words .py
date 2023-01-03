A = str(input("enter 1 string"))
B = str(input("enter 2 string"))

A = A.split()
B = B.split()
x = []
for i in A:
    if i not in B:
        x.append(i)
for i in B:
    if i not in A:
        x.append(i)
x = list(set(x))
print(x)