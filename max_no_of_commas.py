#maximum number of commas
'''  
n=int(input())
c=1000
comma=1
res=0
while c<=n:
    m=c*1000
    num=min(n-c+1,m-c)
    res+=num*comma
    c=m
    comma+=1
print(res)
'''

#TYPE 2

'''
n=int(input())
i=0
while n!=0:
    r=n%1000
    i+=1
    n=n//1000
print(i)
'''