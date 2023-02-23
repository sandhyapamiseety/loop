#          1
#        2 1
#      3 2 1
#    4 3 2 1
#  5 4 3 2 1


i=1
while i<=5:
    k=1
    while k<=5-i:
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=1:
        print(j,end=" ")
        j=j-1
    i=i+1
    print()