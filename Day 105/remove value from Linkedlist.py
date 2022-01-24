# Github: Shantanugupta1118
# DAY 105 of DAY 100
# Remove Value from Linkedlist



class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        # Push element to the LL
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        
        # Print LL
    def display(self):
        if not self.head:
            return
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
            
            
        # Remove targeted Node from LL    
    def removeNode(self, val):
        def deleteNode():
           temp = self.head
           while temp.data is not val:
               temp = temp.next 
           temp.data = temp.next.data
           temp.next = temp.next.next           
                   
            
        if not self.head: return
        count_occurance = 0
        temp = self.head
        # count occurances of the targeted node
        while temp:
            if temp.data == val: 
                count_occurance += 1
            temp = temp.next
        temp = self.head
        print()
        for _ in range(count_occurance): 
            deleteNode()
                    
        
    
    
    
    
    
# -------Main Driver--------
llist = LinkedList()
arr = [7,1,3,2,3,5,6,7,4,3]

for i in arr:
    llist.push(i)
    
print ("Created Linked List: ")
llist.display() 
llist.removeNode(3) 
print ("\nLinked List after Deletion of 3:")
llist.display() 
            
        