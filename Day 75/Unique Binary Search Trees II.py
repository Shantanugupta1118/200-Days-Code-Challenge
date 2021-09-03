# Github: Shantanugupta1118
# DAY 65 of DAY 100
# 95. Unique Binary Search Trees II - Leetcode
# https://leetcode.com/problems/unique-binary-search-trees-ii/


from itertools import product

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        def node_traverse(s,e):
            if s>e:
                return [None]
            if s==e:
                return [TreeNode(s)]
            return_list = []
            for i in range(s,e+1):
                left = node_traverse(s, i-1)
                right = node_traverse(i+1, e)
                for p in product(left, right):
                    return_list.append(TreeNode(i, p[0], p[1]))
            return return_list
        
        return node_traverse(1, n)