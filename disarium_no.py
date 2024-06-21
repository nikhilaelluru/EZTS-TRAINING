# Disarium number 

'''
n=int(input())
temp=n
m=n
c=0
sum=0
while n>0:
    c=c+1
    n=n//10
    
while temp>0:
    rem=temp%10
    sum=sum+rem**c
    c=c-1
    temp=temp//10

print(sum)  
  '''