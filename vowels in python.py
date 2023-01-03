sen = str(input("enter sentence : "))

low_sen = sen.lower()

count = 0

list = ['a','e','i','o','u']
vowels = []

for i in low_sen:
    if i in list:
        count += 1
        vowels.append(i)
print('total vowels count = ', count)
print("vowels are =",vowels)







