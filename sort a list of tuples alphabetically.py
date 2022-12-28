lt = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]

lnt = len(lt)
for i in range(lnt):
    for j in range(lnt-i-1):
        if lt[j][0] > lt[j+1][0]:
            lt[j],lt[j+1] = lt[j+1],lt[j]
print(lt)
