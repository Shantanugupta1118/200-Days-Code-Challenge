# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = tail = ListNode()
        tail.next = head
        while tail.next and tail.next.next:
            first = tail.next
            second = tail.next.next
            third = tail.next.next.next
            
            tail.next = second
            tail.next.next = first
            tail.next.next.next = third
            tail = first
        return prev.next
