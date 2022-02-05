# Github: Shantanugupta1118
# DAY 116 of DAY 200
# 23. Merge k SOrted Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = None
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(lists,2)
        if len(lists) == 0:
            return None
        
        arr = []
        for i in lists:
            # if len(i) == 0: pass

            while i:
                arr.append(i.val)
                print(i.val)
                i = i.next
        arr.sort()
        
        for i in reversed(arr):
            new_node = TreeNode(i)
            # 3. Make next of new Node as head
            new_node.next = self.head
            # 4. Move the head to point to new Node
            self.head = new_node
        return self.head

    
    
print(Solution().solve())

