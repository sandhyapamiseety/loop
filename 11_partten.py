#    1
#    2 1
#    3 2 1
#    4 3 2 1
#    5 4 3 2 1


a=int(input("enter the number"))
i=1
while i<=5:
    print(" ",end= " ")
    j=i
    while j>=1:
        print(j,end= " ")
        j=j-1
    i=i+1
    print()
    