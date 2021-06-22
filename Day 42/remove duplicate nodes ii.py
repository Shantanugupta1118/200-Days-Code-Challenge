# Github: Shantanugupta1118
# DAY 42 of DAY 100
# 83. Remove Duplicates from Sorted List    -  LeetCode/LinkedList
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/



class Node:
    def __init__(self, data=0) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def disp(self):
        if self.head is None:
            return None 
        curr = self.head
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()

    


ll = LinkedList()
arr = [1,2,2,3,5,6,6,7,8,9,9,10,12]
for i in arr:
    ll.push(i)
ll.disp()