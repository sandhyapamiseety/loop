#           *
#         * * *
#       * * * * *
#         * * *
#           *



a=int(input("enter the number"))
i=1
while i<=a:
    k=1
    while k<=a-i:
        print("",end=" ")
        k=k+1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+2
    print()
i=3
while i>=1:
    k=1
    while k<=5-i:
        print("",end=" ")
        k=k+1
    j=i
    while j>=1:
        print("*",end=" ")    
        j=j-1
    i=i-2
    print()