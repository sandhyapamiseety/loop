# a=int(input("enter the number"))
# i=1
# while i<=a:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",j*i)
#         j=j+1
#     i=i+1
#     print()



a=int(input("enter the number"))
i=1
while i<=10:
    j=1
    while j<=a:
        print(j,"*",i,"=",j*i,end="    ")
        j=j+1
    i=i+1
    print()    



# a=int(input("enter the number"))
# i=10
# while i>=1:
#     j=a
#     while j>=1:
#         print(j,"*",i,"=",j*i,end="    ")
#         j=j-1
#     i=i-1
#     print()  