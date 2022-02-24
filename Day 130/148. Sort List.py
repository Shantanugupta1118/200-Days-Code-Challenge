# Github: Shantanugupta1118
# DAY 130 of DAY 200
# 148. Sort List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        arr.sort()
        head = None
        for i in reversed(arr):
            n = ListNode(i)
            n.next = head
            head = n
        return head
