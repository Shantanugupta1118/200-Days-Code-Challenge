# Github: Shantanugupta1118
# DAY 25 of DAY 100
# 894. All Possible Full Binary Trees
# https://leetcode.com/problems/all-possible-full-binary-trees/

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass
        
    def copy_nodes(self, node):
        if not node:
            return None
        new_node = TreeNode(node.data)
        new_node.left = self.copy_nodes(node.left)
        new_node.right = self.copy_nodes(node.right)
        return new_node

    def FBT(self, n: int):
        arr = [[] for i in range(n+1)]
        arr[1] = [TreeNode(0)]
        for i in range(3, n+1):
            for j in range(i-1):
                for node_left in arr[j]:
                    for node_right in arr[i-j-1]:
                        arr[i].append(TreeNode(0, self.copy_nodes(node_left), self.copy_nodes(node_right)))

        return arr[n]



n = int(input())
print(Solution().FBT(n))