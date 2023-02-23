# a=int(input("enter the number"))
# i=1
# while i<=a:
#     k=1
#     while k<=1:
#         print("",end=" ")
#         k=k+1
#         j=1
#         while j<=i:
#           print("*",end=" ")
#           j=j+2
#         i=i+2
#         print()









# i=1
# a=1
# while i<=5:
#     j=1
#     while j<=5:
#         print(a,end=" ")
#         a=a+1
#         j=j+1
#     i=i+1
#     print()





i=1
while i<=5:
    k=0
    while k<=5-i:
        print(" ",end="")
        k=k+1
    j=i
    while j>=1:
       if j>1:
         print(i,end="")
       else:
         print(1,end="")
       j=j-1
    m=2
    while m<=i:
        print(i,end="")
        m=m+1
    i=i+1
    print()