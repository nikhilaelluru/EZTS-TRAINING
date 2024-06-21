# Armstrong Number - Type 1

''' num=int(input("Enter number"))
digit=len(str(num))
sum=0
temp=num
nik=num
while temp>0:
    n=temp%10
    sum=sum+n**digit
    temp=temp//10
if nik==sum:
    print("armstrong number")
else:
    print("not armstrong") '''
 
 
# Type 2  

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
    temp=temp//10
    
if sum==m:
    print("armstrong")
else:
    print("not armstrong")  
'''   
