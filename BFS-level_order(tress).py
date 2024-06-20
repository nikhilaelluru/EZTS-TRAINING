#BREADTH FIRST SEARCH-[BFS]
'''
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None 
        
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
                
# TO FIND HEIGHT OF ANY TREE
def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return (max(lh,rh)+1)

#TO FIND THE LEAF NODES
def print_leaf_node(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        print(root.data)
        return
    print_leaf_node(root.left)
    print_leaf_node(root.right)
                      
if __name__=="__main__":
    root=(node(1))
    
    root.left=node(2)
    root.right=node(3)
    
    root.left.left=node(4)
    root.left.right=node(5)
    
    root.right.left=node(6)
    root.right.right=node(7)
    
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)  
    
    print("LEVEL ORDER")
    level_order(root)
    print("\nheight of tree")
    print(height(root))
'''
