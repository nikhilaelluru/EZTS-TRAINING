
# In a factory many workers are working there each worker is assigned with a integer number help them to 
# find their supervisor. The project manager having an array that cosists if a integer numbers help the
# project manager to find their supervisors. Supervisor will be assigned as the first largest integer
# find on the right side of the array if not found return -1.

# i/p:[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
# o/p:[5,14,14,-1,7,7,9,-1,9,9,-1,5,5,-1,-1]

# if empty   ->  -1
# if smaller -> remove, if stack is empty print -1, if bigger ele present than curr ele return bigger ele which is on top of stack.
# if bigger  -> return result and add current element to the stack
# above three conditions are possible only if stack! empty or top > element

# -> add current element to the stack

# time complexity: O(n)

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
    def top(self):
        return self.items[-1]
    
s=stack()
ip=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
o=[0]*len(ip)
for i in range(len(ip)-1,-1,-1):
    if s.size()!=0:
        while s.size()!=0 and s.top() <= ip[i]:
            if s.top()<=ip[i]:
                s.pop()
    if s.size()==0:
        o[i]=-1
    else:
        o[i]=s.top()
    s.push(ip[i])
print(o)
'''