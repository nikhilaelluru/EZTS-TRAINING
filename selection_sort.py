#SELECTION SORT

'''
l=list(map(int,input().split()))
for i in range(0,len(l)):
    pos=i
    min=l[i]
    for j in range(i+1,len(l)):
        if l[j]<min:
            min=l[j]
            pos=j
    l[i],l[pos]=l[pos],l[i]
print(l)
 '''