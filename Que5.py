list1=[1,5,10,12,16,20]
list2=[1,2,10,13,16]
i=0
l=[]
a=list1+list2
while i<len(a):
    b=a[i]
    if b not in l:
        l.append(b)
    i=i+1
print(l)