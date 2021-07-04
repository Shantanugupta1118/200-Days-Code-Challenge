
# Github: Shantanugupta1118
# DAY 50 of DAY 100
# 86. Partition List - Leetcode/LinkedList
# https://leetcode.com/problems/partition-list/

'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 

class LinkediList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def disp(self):
        if self.head is None:
            return None
        curr = self.head
        while curr:
            print(curr.data, end= ' ')
            curr = curr.next
        print()

    def partition(self, x):
        def merge(small, high):
            res = LinkediList()
            curr = small.head
            while curr:
                res.push(curr.data)
                curr = curr.next
            curr = high.head
            while curr:
                res.push(curr.data)
                curr = curr.next
            return res

        curr = self.head
        small = LinkediList()
        high = LinkediList()
        while curr:
            if curr.data < x:
                small.push(curr.data)
            else:
                high.push(curr.data)
            curr = curr.next
        return merge(small, high)
'''

class Node:
    def __init__(self, data=None):
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
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def disp(self):
        if self.head is None:
            return None
        curr = self.head
        while curr:
            print(curr.data, end= ' ')
            curr = curr.next
        print()

    def partition(self, x):
        curr = self.head
        small_list = s = Node(0)
        large_list = l = Node(0)
        while curr:
            if curr.data < x:
                s.next = curr
                s = s.next
            else:
                l.next = curr
                l = l.next
            curr = curr.next

        l.next = None
        s.next = large_list.next
        return small_list.next




ll = LinkedList()
arr = [1, 4, 3, 2, 5, 2]
for i in arr:
    ll.push(i)
ll.disp()
a = ll.partition(3)
a.disp()
