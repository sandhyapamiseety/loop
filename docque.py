a=int(input("enter the number"))
i=2
sum=1
while i<=a:
    if i%2==0:
       sum=sum+(i**2)
       print(i)
    else:
       sum=sum-(i**2)
       print(i)
    i=i+1
print(sum)