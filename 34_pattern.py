#           1
#         2 3
#       3 4 5
#     4 5 6 7
#   5 6 7 8 9



i=1
while i<=5:
    k=1
    while k>=i-5:
        print(" ",end=" ")
        k-=1
    j=1
    while j<=i:
        print(j-1+i,end=" ")
        j+=1
    i+=1
    print()