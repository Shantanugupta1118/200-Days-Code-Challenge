# Github: Shantanugupta1118
# DAY 44 of DAY 100
# 141. Linked List Cycle I -  LeetCode/LinkedList
# https://leetcode.com/problems/linked-list-cycle/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                return True
            if fast is None:
                return False
            
        return False