# A student is given a task to create some mathematical expression for BODMAS. But due to some other work 
# he forgot to do that but in the night he clicked that he have to create some expression for BODMAS due 
# to sleepy mood he did some mistake while putting the brackets. Your job is to check whether expression 
# given by the boy is valid or not.

# sample Input:
# [3+7{52/11(3+5)}]  valid expression as all the brackets are properly open and close.

# [4-6]{235(9+6)]   invalid expression as some brackets are not proper.

'''
class stack:
    def __init__(self):
        self.items=[]
    def push(self,b):
        self.items.append(b)
    def pop(self):
        return self.items.pop()
    
s=stack()
exp=input()
flag=True
for i in exp:
    if i=="(" or i=="{" or i=="[":
        s.push(i)
    elif i==")" or i=="}" or i=="]":
       r=s.pop()
       if(i==")" and r!="(") or (i=="}" and r!="{") or (i=="]"):
            flag=False
            break
        
if flag:
    print("valid")
else:
    print("Invalid")
 '''   
  
#TYPE2

'''
class stack:
    def __init__(self):
        self.items=[]
    def push(self,b):
        self.items.append(b)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        
e=input()

s=stack()
ob="[{("
cb=")}]"
flag=0
for i in e:
    if i in ob:
        s.push(i)
    if i in cb:
        x=s.pop()
        if x=="(" and i==")":
            pass  
        elif x=="{" and i=="}":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag=1
            break
if flag==0 and s.size()==0:
    print("valid")
else:
    print("invalid")
    '''

#TYPE3
'''
def balnce(n):
    l=''
    b="[](){}"
    for i in n:
        if i in b:
             l+=i
    print(l)
    if l[0]==")" or l[0]==']' or l[0]=='}':
        return "invalid"
    else:
        while '()' in  l or  '[]' in l or '{}' in l:
                l=l.replace('()',"").replace('[]',"").replace('{}',"")
        print(len(l))
        if len(l)==0:
            return "valid"
        else:
            return "invalid"
n=input()
print(balnce(n))
'''