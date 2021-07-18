# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def check(self, head, k):
        i = 1
        while head and i <= k:
            head = head.next
            i += 1
        if i > k:
            return True
        return False
        
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
		#check if k more nodes are present
		#just reverse next k nodes
        if self.check(head, k):
            curr = head
            i = 1
            prev = None
            while i<=k and curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
                i += 1
			#now recursively compute head.next
            head.next = self.reverseKGroup(curr, k)
			#prev will be the new head now
            return prev
        return head