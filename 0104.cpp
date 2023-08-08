class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root)
            return 0;

        int l = 1 + maxDepth(root->left);
        int r = 1 + maxDepth(root->right);
        return l < r ? r : l;
    }
};
