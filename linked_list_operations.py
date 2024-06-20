#LINKED LIST OPERATIONS

class Node:
    def _init_(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None
    
    def insert_front(self):
        n = int(input("Enter the element: "))
        temp = Node(n)
        if self.head==None:
            self.head = self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        self.print_link_list()

    def insert_end(self):
        n = int(input("Enter the element: "))
        temp = Node(n)
        if self.head==None:
            self.head = self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.print_link_list()

    def insert_any(self, position):
        n = int(input("Enter the element: "))
        temp = Node(n)
        if position == 0:
            temp.next = self.head
            self.head = temp
            if self.tail==None:  
                self.tail = temp
        else:
            curr = self.head
            for i in range(position - 1):
                if curr is None:
                    print("Position out of bounds")
                    return
                curr = curr.next
            temp.next = curr.next
            curr.next = temp
            if temp.next==None:  
                self.tail = temp
        self.print_link_list()

    def delete_front(self):
        if self.head==None:
            print("List is empty")
        else:
            self.head = self.head.next
            if self.head==None:  
                self.tail = None
        self.print_link_list()

    def delete_end(self):
        if self.head==None:
            print("List is empty")
        elif self.head.next==None:
            self.head = self.tail = None
        else:
            curr = self.head
            while curr.next.next!=None:
                curr = curr.next
            curr.next = None
            #self.tail = curr
        self.print_link_list()

    def delete_any(self, position):
        if self.head is None:
            print("List is empty")
        elif position == 0:
            self.head = self.head.next
            if self.head is None:  
                self.tail = None
        else:
            curr = self.head
            for i in range(position - 1):
                if curr is None or curr.next is None:
                    print("Position out of bounds")
                    return
                curr = curr.next
            if curr.next is None:
                print("Position out of bounds")
                return
            curr.next = curr.next.next
            if curr.next is None:  
                self.tail = curr
        self.print_link_list()
    
    def print_link_list(self):
        if self.head==None:
            print("List is empty")
            return 
        curr = self.head
        while curr!=None:
            print(curr.value)
            curr = curr.next

ll = LinkedList()
while True:
        print("\nMenu:")
        print("1. Insert at front")
        print("2. Insert at end")
        print("3. Insertion anywhere")
        print("4. Delete from front")
        print("5. Delete from end")
        print("6. Deletion anywhere")
        print("7. Print list")
        print("8. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            ll.insert_front()
        elif choice == 2:
            ll.insert_end()
        elif choice == 3:
            position = int(input("Enter the position: "))
            ll.insert_any(position)
        elif choice == 4:
            ll.delete_front()
        elif choice == 5:
            ll.delete_end()
        elif choice == 6:
            position = int(input("Enter the position: "))
            ll.delete_any(position)
        elif choice == 7:
            ll.print_link_list()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice")
