# PRIME NUMBER
'''m=int(input("Enter message: "))
flag=0
if m<1:
    flag=1
elif m==1:
    flag=0
else:
    for i in range(2,m):
        if m%i==0:
            flag=1
            break
if flag==0:
    print("valid message")
else:
    print("invalid message")'''
    
    
#TYPE 2
  
'''m=int(input("Enter message: "))
flag=0
if m<1:
    flag=1
elif m==1:
    flag=0
else:
    for i in range(2,(m//2)+1):
        if m%i==0:
            flag=1
            break
if flag==0:
    print("valid message")
else:
    print("invalid message")'''
    
#---------------------------------------------------------------------------------------------

#Fibonacci Series
   
'''def f(n):
    if n==0:
        return 0
    if n==1: 
        return 1
    else:
        return f(n+1)+f(n+2)
n=int(input())
print(f(n))'''

#Type 2
'''int(input("Enter number of terms:"))
a=0
b=1
c=a+b
if n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
        print(c)
        a=b
        b=c
        c=a+b'''