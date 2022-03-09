class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        curr = ListNode(None)
        ans = curr
        
        while head:
            if head.val != prev and (head.next is None or head.val != head.next.val):
                curr.next = head
                curr = curr.next
            else:
                curr.next = None
            prev = head.val    
            head = head.next
            
        return ans.next