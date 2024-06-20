#LINKED LIST

'''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None        

head=tail=node(10)
tail.next=node(20)
tail=tail.next

tail.next=node(30)
tail=tail.next        
        
tail.next=node(40)
tail=tail.next

def print_link_list(head):
    if head==None:
        print("List is empty")
        return
    curr=head
    while curr!=None:
        print(curr.data)
        curr=curr.next
        
print(head)
print(tail)
print(head.next.next.next)
print(print_link_list(head))

'''