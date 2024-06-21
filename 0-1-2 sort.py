#[2,1,0,1,1,2,0,0] => [0,0,0,1,1,1,2,2] (0-1-2 sort)

'''a=[2,1,0,1,1,2,0,0]
c1=0
c2=0
c3=0
for i in range(len(a)):
    if a[i]==0:
        c1=c1+1
    elif a[i]==1:
        c2=c2+1
    else:
        c3=c3+1
j=0

while c1>0:
    a[j]=0
    j=j+1
    c1=c1-1
    
while c2>0:
    a[j]=1
    j=j+1
    c2=c2-1
    
while c3>0:
    a[j]=2
    j=j+1
    c3=c3-1
    
print(a)                     '''
