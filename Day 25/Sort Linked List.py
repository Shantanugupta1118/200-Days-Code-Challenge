# Github: Shantanugupta1118
# DAY 25 of DAY 100
# Sort Linked List - InterviewBit/Google
# https://www.interviewbit.com/problems/sort-list/


from collections import deque 

class Node:
    def __init__(self, data):
        self.data = data
        self. next = None

class Solution:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node


    # LIST METHOD
    '''
    def sorting(self):
        value = []
        temp = self.head

        while self.head:
            value.append(self.head.data)
            self.head = self.head.next
        
        value.sort()
        value = deque(value)

        self.head = temp
        while temp:
            temp.data = value.popleft()
            temp = temp.next
        '''
        
    # Direct LinkedList Sort
    def sorting(self):
        if self.head is None:
            return
        else:
            curr = self.head
            idx = None 
            while curr != None:
                idx = curr.next
                while idx != None:
                    if curr.data > idx.data:
                        curr.data, idx.data = idx.data, curr.data
                    idx = idx.next
                curr = curr.next

    def display(self):
        if self.head is None:
            return None
        else:
            curr = self.head
            while curr:
                print(curr.data, end= ' -> ')
                curr = curr.next
            print("NULL\n\n")




# TEST CASES-------------------------------
ll = Solution()
arr = [3,5,2,1,4,7]
for i in arr:
    ll.push(i)
print("-------- ARRAY 1 --------")
ll.display()
ll.sorting()
ll.display()

ll2 = Solution()
arr2 = [5,2,9,6,7,4,1]
for i in arr2:
    ll2.push(i)
print("-------- ARRAY 2 --------")
ll2.display()
ll2.sorting()
ll2.display()


ll3 = Solution()
arr3 = [2,3,4,5,6,7]
for i in arr3:
    ll3.push(i)
print("-------- ARRAY 3 --------")
ll3.display()
ll3.sorting()
ll3.display()