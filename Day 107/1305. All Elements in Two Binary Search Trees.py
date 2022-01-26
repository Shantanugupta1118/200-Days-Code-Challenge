# Github: Shantanugupta1118
# DAY 107 of DAY 100
# 1305. All Elements in Two Binary Search Trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1, root2):
        arr1, arr2 = [], []
        self.inorder(root1, arr1)
        self.inorder(root2, arr2)
        print(arr1, arr2)
        return sorted(arr1+arr2)
        
    def inorder(self, root, arr):
        if not root: return
        else:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
        return arr
        
