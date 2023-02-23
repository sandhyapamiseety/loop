#   1 2 3 4 5
#     1 2 3 4
#       1 2 3
#         1 2
#           1



i=1
while i<=6:
    k=1
    while k<=i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=6-i:
        print(j,end=" ")
        j=j+1
    i=i+1
    print()
        