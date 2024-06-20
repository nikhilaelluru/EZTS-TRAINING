#INSERTION SORT

'''
l=list(map(int,input().split()))
n=len(l)
for i in range(1,len(l)):
    ele=l[i]
    index=i
    for j in range(i-1,-1,-1):
        if ele<l[j]:
            l[j+1]=l[j]
            index=j
        else:
            break
    l[index]=ele
print(l)
'''