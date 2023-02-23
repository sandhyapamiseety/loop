#    5 4 3 2 1 2 3 4 5 
#      4 3 2 1 2 3 4
#        3 2 1 2 3 
#          2 1 2 
#            1  



i=5
while i>=1:
    k=1
    while k<=5-i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i:
        print(i-j+1,end=" ")
        j=j+1
    m=2
    while m<=i:
        print(m,end=" ")
        m=m+1
    i=i-1
    print() 
