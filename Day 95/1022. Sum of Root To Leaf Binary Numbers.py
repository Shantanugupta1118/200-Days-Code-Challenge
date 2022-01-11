# Github: Shantanugupta1118
# DAY 65 of DAY 100
# 1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root):
        self.ans=0
        def check(node,s):

            if node.left==None and node.right==None:
                s=s+str(node.val)
                self.ans=self.ans+int(s,2)
                return

            s=s+str(node.val)

            if node.left!=None:
                check(node.left,s)

            if node.right!=None:
                check(node.right,s)

        check(root,'')
        return self.ans

        
for _ in range(int(input())):
    print(Solution().sumRootToLeaf([1,0,1,0,1,0,1]))