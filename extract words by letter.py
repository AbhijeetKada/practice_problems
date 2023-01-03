test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
K = str(input("enter the letter"))
res = []
for sub in test_list:
    temp = sub.split()
    for ele in temp:
        if ele[0].lower() == K.lower():
            res.append(ele)

print(str(res))
