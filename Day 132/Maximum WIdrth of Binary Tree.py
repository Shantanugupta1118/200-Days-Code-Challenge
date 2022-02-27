# Github: Shantanugupta1118
# DAY 132 of DAY 200
# 662. Maximum Width of Binary Tree



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def widthOfBinaryTree(self, root):
        q = [[root, 0]]
        node = TreeNode()
        ans = -1
        while not len(q)==0:
            size = len(q)
            mmin = q[-1][1]
            first, last = 0, 0
            for i in range(size):
                curr_id = q[-1][1]-mmin
                node = q[-1][0]
                q.pop()
                if i==0: first = curr_id
                if i==1: last = curr_id
                if node.left: 
                    q.append([node.left, curr_id*2+1])
                if node.right:
                    q.append([node.right, curr_id*2+2])
                print(q)
            ans = max(ans, last-first+1)
        return ans
                
        