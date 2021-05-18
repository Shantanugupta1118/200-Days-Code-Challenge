// # Github: Shantanugupta1118
// # DAY 10 of DAY 100
// # LC - Path Sum - 112
// # https://leetcode.com/problems/path-sum/

/*

bool hasPathSum(TreeNode* root, int targetSum) {
    if(!root) return false;
   if(!root->left && !root->right){
        if(root->val==targetSum) return true;
        return false;
    }
    
    bool ans=false;
    if(root->left)
       ans=ans || hasPathSum(root->left,targetSum-root->val);
    if(root->right)
     ans=ans || hasPathSum(root->right,targetSum-root->val);
    return ans;
}

*/