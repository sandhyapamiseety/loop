#  U V W X Y
#  P Q R S T 
#  K L M N O 
#  F G H I J 
#  A B C D E



a=int(input("enter the number"))
i=0
k=84+1
while i<=a:
    j=0
    while j<=a:
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    k=k-10
    i=i+1
    print()