# n=input()
# i=0
# sum=0
# while i<len(n):
#      sum=sum+int(n[i])
#      i=i+1   
# if int(n)%sum==0:
#    print(n,"harshad number")
# else:
#    print("not harsada number") 


#         (or) 
# a=int(input("enter the number"))
# sum=0
# x=a
# while x>0:
#     r=x%10
#     sum=sum+r
#     x=x//10
# if x%sum==0:
#      print("harsad number" ,a)
# else:
#     print("not harsad number",a)  
    


i=1
while i<5:
    print(" "*(5-i),end=" ")
    j=1
    while j<=i:
        print(1*(j+1),end="")
        j=j+1
    i=i+1
    print()
