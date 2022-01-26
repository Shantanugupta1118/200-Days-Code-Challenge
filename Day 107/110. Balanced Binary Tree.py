# Github: Shantanugupta1118
# DAY 107 of DAY 100
#110. Balanced Binary Tree


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
        
    def getNode(self, data):
        newNode = TreeNode(data)
        newNode.val = data
        newNode.left = None
        newNode.right = None
        return newNode

    def levelOrder(self,root, data):
        if root == None:
            root = self.getNode(data)
            return root
        if data <= root.val:
            root.left = self.levelOrder(root.left, data)
        else:
            root.right = self.levelOrder(root.right, data)
        return root
   
    def constructBST(self, arr, n):
        if n == 0: return None
        root = None
        for i in range(n):
            root = self.levelOrder(root, arr[i])
        return root
    
    
    
    
# ---------- MAIN DRIVER -----------
arr1 = [7,8,4,12,3,6,8,1,5,10]
n = len(arr1)
root1 = Solution().constructBST(arr1, n)

arr2 = [9,6,2,4,74,1,2,5]
n1 = len(arr2)
root2 = Solution().constructBST(arr2, n1)

root = Solution().getAllElements(root1, root2)
print("Merged BST: ", root)
    
    
    