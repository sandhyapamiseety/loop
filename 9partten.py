#            1 
#          2 2
#        3 3 3
#      4 4 4 4
#    5 5 5 5 5


i=1
while i<=5:
    k=1
    while k<=5-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1
    print()