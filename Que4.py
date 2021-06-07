list1=[1,342,75,23,98,]
list2=[74,23,98,12,78,10,1]
i=0
l=[]
while i<len(list2):
    a=list2[i]
    if a in list1:
        l.append(a)
    i=i+1
print(l)