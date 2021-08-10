//# Github: Shantanugupta1118
//# DAY 71 of DAY 100
// 113. Path Sum  - leetcode/August
// https://leetcode.com/problems/path-sum-ii/


/*--- Header Files---*/
#include<iostream>
#include<bits/stdc++.h>
#include<cmath>
#include<string>

using namespace std;

/*---Defines ---*/
#define itr(s,e,t) for(int i=s; i<e; i=i+t)
#define itr1(s,e,t) for(int i=s; i<=e; i=i+t)
#define rev_itr(s,e,t) for(int i=e; i>s; i=i-t)



struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    void findSum(TreeNode* root, int target, int prev_sum, vector<int> current_node) {
        if(!root) {
            return;
        }
        prev_sum += root->val;
        current_node.push_back(root->val);

        if(prev_sum == target && !root->left && !root->right) {
            res.push_back(current_node);
        }
        findSum(root->left, target, prev_sum, current_node);
        findSum(root->right, target, prev_sum, current_node);
        current_node.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        int prev_sum = 0;
        findSum(root, targetSum, 0, {});
        return res;
    }
    private:
        vector<vector<int>> res;
};

