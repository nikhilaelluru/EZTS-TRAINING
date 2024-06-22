#AVL TREE
'''
class node:                                   #class for tree node
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.height=1
        
def inorder(root):                             #print the data in inorder format
    if not root:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
    
def insert(root,ele):
    if not root:
        return node(ele)
    if ele<root.val:
        root.left=insert(root.left,ele)
    else:
        root.right=insert(root.right,ele)
       
    root.height=1+max(ght(root.left),ght(root.right)) 
    
    bf=getbf(root)
    
    if bf>1 and ele < root.left.val:              #RR ROTATION
        return rightrotate(root)
    
    if bf>1 and ele > root.left.val:
        root.left=leftrotate(root.left)           #RL ROTATION
        return rightrotate(root)
    
    if bf<-1 and ele > root.right.val:            #LL ROTATION
        return leftrotate(root)

    if bf<-1 and ele < root.right.val:
        root.right=rightrotate(root.right)        #LR ROTATION
        return leftrotate(root)

    return root

def ght(root):
    if not root:
        return 0
    return root.height

def getbf(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)

def leftrotate(a):
    b=a.right                                           #creating a copy of values
    temp=b.left
    
    b.left=a                                            #Rotation  
    a.right=temp             
    
    a.height=1 + max(ght(a.left),ght(a.right))
    b.height=1 + max(ght(b.left),ght(b.right))
    
    return b

def rightrotate(a):
    b=a.left
    temp=b.right
    
    b.right=a
    a.left=temp
    
    a.height=1 + max(ght(a.left),ght(a.right))
    b.height=1 + max(ght(b.left),ght(b.right))   
    
    return b 

        
if __name__=="__main__":
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    root=None
    for i in vl:                                        #vl-value_list
        root=insert(root,i)
    inorder(root)
    '''