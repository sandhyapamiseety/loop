# a=int(input())
# i=1
# while i<=a:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     k=1
#     while k<=i:
#           print("*",end=" ")
#           k=k+1
#     i=i+1
#     print()

i=1
k=65
while i<=5:
    j=1
    while j<=i:
        print(chr(k),end=" ")
        print(i)
        j=j+1
    i=i+1
    k=k+1
    print()
    
