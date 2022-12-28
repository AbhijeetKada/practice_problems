n=str(input("enter string"))

s=n.split(" ")

for i in s:
  if len(i)%2==0:
    print(i)