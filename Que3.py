list=["usha","usha","mona","niki","niki","anvi"]
i=0
l=[]
while i<len(list):
    a=list[i]
    if a not in l:
        l.append(a)
    i=i+1
print(l)
