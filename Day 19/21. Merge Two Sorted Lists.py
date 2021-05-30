# Contribution By: Shantanu Gupta
# Github: Shantanugupta1118
# DAY 19 of DAY 100
# 21. Merge Two sorted lists
# https://leetcode.com/problems/merge-two-sorted-lists/


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
    
    def mergeTwoLists(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        l3 = ListNode(0)
        curr, curr1, curr2 =l3, l1, l2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next
            curr = curr.next
        curr.next = curr1 if curr2 is None else curr2
        return l3.next

        



l1 = Solution()
l2 = Solution()
l3 = Solution()
arr1 = [1,2,4]
arr2 = [1,3,4]
for i in arr1:
    l1.push(i)
for i in arr2:
    l2.push(i)
    
l1.display()
l2.display()
x = Solution().mergeTwoLists(l1, l2)
x.display()