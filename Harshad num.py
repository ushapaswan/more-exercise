n=int(input("enter the number"))
i=0 
s=n
r=sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
if s%sum==0:
    print("harshad number")
else:
    print("not harshad")