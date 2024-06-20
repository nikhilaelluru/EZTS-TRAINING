#BUBBLE SORT

#Write a code to find minimum element out of given elements.
'''
l=list(map(int,input().split()))
n=len(l)
for j in range(0,n):
    for i in range(0,n-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)
'''