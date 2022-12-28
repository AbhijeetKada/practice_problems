# req ANS ::: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# ANS ::
i_p = ['p','q']

n =5
fnl = []

for i in i_p:
    for j in range(1,n+1):
        fnl = ['{}{}'.format(x,y) for y in range(1,n+1) for x in i_p]
print(fnl)