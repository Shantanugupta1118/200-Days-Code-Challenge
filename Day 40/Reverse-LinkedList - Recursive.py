# Github: Shantanugupta1118
# DAY 40 of DAY 100
# Reverse LinkedList Iterative  -  LinkedList


class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None 
    
class LinkedList:
    # Initializing Head Node
    def __init__(self):
        self.head = None

    # Push new Data into New Node of LinkedList
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node


    def disp(self):
        if self.head is None:
            return None 
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()

    # Recursive Reverse 
    def reverse_recursive(self):
        def reverseNode(prev, curr):
            if curr is not None:
                reverseNode(curr, curr.next)
                curr.next = prev
            else:
                self.head = prev
        reverseNode(None, self.head)


# main driver
ll = LinkedList()
arr = [int(x) for x in range(1, 10)]
for i in arr:
    ll.push(i)
ll.disp()
ll.reverse_recursive()
ll.disp()