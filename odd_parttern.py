#  1 
#  3 5
#  7 9 11 






a=int(input("enter the number"))  
i=1
k=1
while i<=a:
    j=1
    while j<=i:
        if j%2!=0:
            print(k,end=" ")
        else:
            print("")
        j=j+2
        k=k+2
    i=i+2
    print()