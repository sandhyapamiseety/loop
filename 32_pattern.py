#                    0
#                  1 0 1
#                2 1 0 1 2
#              3 2 1 0 1 2 3 
#            4 3 2 1 0 1 2 3 4 
#          5 4 3 2 1 0 1 2 3 4 5  


i=0
while i<=5:
    k=1
    while k<=5-i:
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=0:
        print(j,end=" ")
        j=j-1
    m=1
    while m<=i:
        print(m,end=" ")
        m=m+1
    i=i+1
    print()