# Github: Shantanugupta1118
# DAY 107 of DAY 100
# 110. Balanced Binary Tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # ------- Check Height --------
    def height(self, root):
        if not root: return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    # ----------- Check Balance of BST ----------
    ''' 
            First Approach --- 
                Passed 183 cases out of 288
    '''
    '''
    def checkBalance(self, root):
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        if abs(left_height-right_height <= 1) and self.checkBalance(root.left) and self.checkBalance(root.right):
            return True
        return False
    '''
    
    # ---- Second Approach ---------
    ''' Accepted all cases'''
    def checkBalance(self, root):
        if not root: return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        return self.checkBalance(root.left) and self.checkBalance(root.right)
    
    def inorder(self, root, arr):
        if not root:
            return
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

print("balance BST: ", Solution().checkBalance(root1))
print("balance BST: ", Solution().checkBalance(root2))
    
    
    