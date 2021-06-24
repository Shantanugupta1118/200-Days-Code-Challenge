# Github: Shantanugupta1118
# DAY 43 of DAY 100
# 138. Copy List with Random Pointer  -  LeetCode/LinkedList
# https://leetcode.com/problems/copy-list-with-random-pointer/



"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        ptr = head
        while ptr:
            new_node = Node(ptr.val, ptr.next, None)
            ptr.next = new_node
            ptr = new_node.next
        ptr = head
        
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random is not None else None
            ptr = ptr.next.next
        old = head
        new = head.next
        new_head = new
        
        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next is not None else None
            old = old.next
            new = new.next
            
        return new_head


