a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b>c or a>c>b:
    print(a,"is maximum")
elif b>c>a or b>a>c:
    print(b,"is maximum")
elif c>a>b and c>b>a:
    print(c,"is maximu