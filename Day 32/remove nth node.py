# username: shantanugupta1118
# Day 32 of 100 Days
# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/



class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start, curr = [], head
        while curr:
            start.append(curr)
            curr = curr.next
        for i in range(n-1):
            start.pop()
        if len(start) == 1:
            return start[0].next
        start[-2].next = start[-1].next
        return head