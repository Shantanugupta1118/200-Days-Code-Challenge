# Github: Shantanugupta1118
# DAY 40 of DAY 100
# Reverse LinkedList Iterative  -  LinkedList


class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
        

class LinkedListNode:
    # Initializing Head Node
    def __init__(self):
        self.head = None
    
    # Push Node into LinkedList
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
    
    # Print Nodes of LinkedList
    def disp(self):
        if self.head is None:
            return None
        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()


    # reverse node
    def reverse_node(self):
        if self.head is None:
            return None
        prevNode = nextNode = None 
        curr = self.head
        while curr is not None:
            nextNode = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = nextNode
        self.head = prevNode
    


# MAIN DRIVER
ll = LinkedListNode()
arr = [int(i) for i in range(1,10)]
for i in arr:
    ll.push(i)
ll.disp()
ll.reverse_node()
ll.disp()
