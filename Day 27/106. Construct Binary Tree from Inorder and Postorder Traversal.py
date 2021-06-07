# Github: Shantanugupta1118
# DAY 27 of DAY 100
# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Solution 2--

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right= None

class Solution:
    def search(self, inorder, val, n):
        i = 0
        while i<n:
            if inorder[i] == val:
                return i
            i += 1
        return i 

    def buildTree(self, inorder, postorder):
        def constructTree(inorder):
            nonlocal postIdx
            if postIdx<0:
                return None
            if inorder==[]:
                return None
            val = postorder[postIdx]
            postIdx -= 1
            inorder_Idx = self.search(inorder, val, len(inorder))
            left_ele = inorder[:inorder_Idx]
            right_ele = inorder[inorder_Idx+1:]
            root = TreeNode(val)
            root.right = constructTree(right_ele)
            root.left = constructTree(left_ele)
            return root

        postIdx = len(postorder)-1
        return constructTree(inorder)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print(Solution().buildTree(inorder, postorder))






# Solution 2---
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    postIdx = 0
    s = []
    def search(self, inorder, val, n):
        i = 0
        while i < n:
            if inorder[i] == val:
                return i
            i += 1
        return i

    def buildTree(self, inorder, postorder, start, end, n):
        if start > end:
            return
        val = postorder[self.postIdx]
        inoIdx = self.search(inorder, val, n)
        self.postIdx -= 1
        self.buildTree(inorder, postorder, inoIdx+1, end, n)
        self.buildTree(inorder, postorder, start, inoIdx-1, n)
        self.s.append(val)


    def constructTree(self, preorder, start, end):
        if start > end:
            return None
        node = Node(preorder[start])
        i = start
        while i <= end:
            if preorder[i] > node.val:
                break
            i += 1
        node.left = self.constructTree(preorder, start+1, i-1)
        node.right = self.constructTree(preorder, i, end)
        return node

    def preOrder(self, inorder, postorder):
        n = len(postorder)
        self.postIdx = n-1
        self.buildTree(inorder, postorder, 0, n-1, n)
        return self.constructTree(self.s, 0, len(self.s)-1)


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print(Solution().preOrder(inorder, postorder))
"""