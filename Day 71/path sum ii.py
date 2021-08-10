# Github: Shantanugupta1118
# DAY 71 of DAY 100
# 113. Path Sum II - Leetcode/August
# https://leetcode.com/problems/path-sum-ii/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, target):
        # recursive function
        def findPathSum(root, target,prev_sum, current):
            if root is None:
                return 
            
            prev_sum += root.val
            current.append(root.val)
            if prev_sum == target and root.left is None and root.right is None:
                self.list_node.append(current[:])
                # return

            findPathSum(root.left, target, prev_sum, current)
            findPathSum(root.right, target, prev_sum, current)
            current.pop()

        # base root
        if root is None:
            return 
        self.list_node = []
        findPathSum(root, target,0, [])
        return self.list_node