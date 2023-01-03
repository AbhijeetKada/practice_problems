str1 = str(input("enter the string"))
count = 0

vowel = set("aeiouAEIOU")

for alphabet in str1:
    if alphabet in vowel:
        count = count + 1

print(count)