# Github: Shantanugupta1118
# DAY 109 of DAY 200
# 237. Delete Node in a Linked List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Add Nodes to the LinkedList
    def push(self, data):
        new_node = TreeNode(data)
        new_node.next = self.head
        self.head = new_node        
        
    # Display Nodes
    def display(self):
        if not self.head: return
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
            
        # Remove targeted Node from LL    
    def removeNode(self, val):
        def deleteNode():
           temp = self.head
           while temp.val != val:
               temp = temp.next 
           temp.data = temp.next.val
           temp.next = temp.next.next           
                   
            
        if not self.head: return
        count_occurance = 0
        temp = self.head
        # count occurances of the targeted node
        while temp:
            if temp.val == val: 
                count_occurance += 1
            temp = temp.next
        temp = self.head
        print()
        for _ in range(count_occurance): 
            deleteNode()        

ll = LinkedList()
arr = [1,2,5,6,3,4]
for i in reversed(arr):
    ll.push(i)
ll.display()
ll.removeNode(5)
ll.display()