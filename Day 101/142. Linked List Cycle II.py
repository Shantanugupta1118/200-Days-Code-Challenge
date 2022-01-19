# Github: Shantanugupta1118
# Day 101 of Day 200
# 142. Linked List Cycle II



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, headNode):
        if not headNode: return None
        slow, fast = head, head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if flag:
            fast = head
            while slow!=fast:
                slow = slow.next
                fast = fast.next
        if flag: return fast
        return -1
