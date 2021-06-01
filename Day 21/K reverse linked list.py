# Github: Shantanugupta1118
# DAY 21 of DAY 100
# K reverse linked list
# https://www.interviewbit.com/problems/k-reverse-linked-list/


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        newNode = ListNode(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
    
    def display(self):
        if self.head is None:
            print("NULL")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=' ')
                curr = curr.next
            print()

    def solve(self, nums, k):
        if k==1:
            return nums
        curr = self.head
        if curr is None or curr.next is None:
            return nums
        ar = []
        while curr:
            ar.append(curr.val)
            curr = curr.next
        temp = []
        for j in range(len(ar)//k):
            temp.extend(ar[:k][::-1])
            del ar[:k]
        curr = self.head
        for i in range(len(temp)):
            curr.val = temp[i]
            curr = curr.next




ll = Solution()

arr = [1,2,3,4,5,6]
k = 2
for i in arr:
    ll.push(i)
ll.display()
ll.solve(arr, k)
ll.display()