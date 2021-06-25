# Github: Shantanugupta1118
# DAY 44 of DAY 100
# 142. Linked List Cycle II -  LeetCode/LinkedList
# https://leetcode.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        
        if flag:
            fast = head
            idx = 0
            while fast!=slow:
                slow = slow.next
                fast = fast.next       
        
        if flag:
            return fast
        
        return None
    
    