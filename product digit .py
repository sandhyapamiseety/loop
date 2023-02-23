n=int(input("enter the number"))
product=1
while n>0:
    a=n%10
    product=a*product
    n=n//10
print(product)
    