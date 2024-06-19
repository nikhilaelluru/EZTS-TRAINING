# Given an integer array your task is to find the 3 continuous digits which gives you the maximum sum.

# sample input: [2,4,3,5,6,3,4,6,7,1,2,5]
# output: [4,6,7]

'''
def max_sum(lst):
    s=[]
    for i in range(len(lst)-2):
        s.append(sum(lst[i:(i+3)]))
    m=s.index(max(s))
    result=lst[m:m+3]
    return result

lst=[2,4,3,5,6,3,4,6,7,1,2,5]
print(lst)
print(max_sum(lst))
'''

#TYPE2

'''l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
for i in range(0,len(l)-2):
    sum=l[i]+l[i+1]+l[i+2]
    if max<sum:
        max=sum
        pos=i
        
print(l[pos],l[pos+1],l[pos+2])
print(max)'''

#--------------------------------------------------------------------------------------------------------------
# Given an integer array your task is to find the k continuous digits which gives you the maximum sum.

# sample input: [2,4,3,5,6,3,4,6,7,1,2,5]
# output: [4,6,7]

'''
def max_sum(k,lst):
    s=[]
    for i in range(len(lst)-(k-1)):
        s.append(sum(lst[i:(i+k)]))
    m=s.index(max(s))
    result=lst[m:m+k]
    return result
    
k=int(input())
#lst=list(map(int,input().split()))
lst=[2,4,3,5,6,3,4,6,7,1,2,5]
print(max_sum(k,lst))
'''

#TYPE2

'''
def max_sum(k,lst):
    m=0
    s=sum(lst[:k])
    for i in range(1,len(lst)-(k-1)):
        m=s-lst[i-1]+lst[i+k-1]
        if s<m:
            s=m
            pos=i
    result=lst[pos:pos+k]
    return result
    
k=int(input("Enter the number of continuous inputs:"))
#lst=list(map(int,input().split()))
lst=[2,4,3,5,6,3,4,6,7,1,2,5]
print(max_sum(k,lst))
'''

#TYPE3
'''
l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
k=int(input("Enter the no of continuous digit: "))
for i in range(0,len(l)-(k-1)):
    sum=0
    for j in range(0,k):
        sum=sum+l[i+j]
    if max<sum:
        max=sum
        pos=i
        
print(max)
for j in range(0,k):
    print(l[pos+j])
    
    '''