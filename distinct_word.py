numbers = int(input('enter total words number'))
input_str = []
while(numbers >0):
    input_str.append(str(input("enter the input string")))
    numbers = numbers - 1
print(input_str)
disct = set(input_str)
print(disct)
print(len(disct))
occr = {}

for i in input_str:
    if i in occr:
        occr[i] = occr[i] + 1
    else:
        occr[i] = 1
for value in occr.values():
    print(value)