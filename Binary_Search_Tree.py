#BINARY SEARCH TREE

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
def binary_search_tree(root,ele):
    if root==None:
        return node(ele)
    if ele<root.value:
        root.left=binary_search_tree(root.left,ele)
    if ele>root.value:
        root.right=binary_search_tree(root.right,ele)
    return root
                      
def preorder(root):
    if root==None:
        return
    
    print(root.value,end=" ")
    preorder(root.left)
    preorder(root.right)
    
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value,end=" ")
    inorder(root.right)
    
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value,end=" ") 
   
def level_order(root):
    q=[root]
    q.append(None)
    
    while len(q)>0:
        curr=q.pop(0)
        
        if curr==None:
            if len(q)==0:
                break
            else:
                print()
                q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
  
def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return (max(lh,rh)+1)

def print_leaf_node(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        print(root.value)
        return
    print_leaf_node(root.left)
    print_leaf_node(root.right) 
    
if __name__=="__main__":
    lst=[4,6,7,3,8,2,5,9,1]
    root=node(lst[0])
    lst.pop(0)
    for i in lst:
        binary_search_tree(root,i)

print("PREORDER")
preorder(root)
print()
print("\nINORDER")
inorder(root)
print()
print("\nPOSTORDER")
postorder(root)
print()
print("\nHEIGHT")
print(height(root))
print()
print("LEVEL ORDER")
level_order(root)
print()
print("\nLEAF NODES")
print_leaf_node(root)

    
  