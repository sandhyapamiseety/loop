num=int(input("enter the number:"))
i=num
sum=0
while (num):
    factorial=1
    r=num%10
    while r:
        factorial=factorial*r
        r=r-1
    sum=sum+factorial
    num=num//10
if sum==i:
    print("strong number",i) 
else:
    print("not strong number",i)






# a=int(input("enter the number"))
# if a>0:
#     b=a%10
#     c=a//10
#     d=c%10
#     e=c//10
#     f=e%10
#     g=d*f
# print(g)    


# a="naga"
# b="suha"
# c=11.19
# d=7
# e=9
# f=3.9
# g=float(d)
# h=g+c
# i=int(f)
# j=h-i
# k=d+e
# print("@",str(j),a,"=",b,"@",str(k))