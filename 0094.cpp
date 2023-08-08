class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (!root)
            return {};

        auto l = inorderTraversal(root->left);
        auto r = inorderTraversal(root->right);

        vector<int> result(l.begin(), l.end());
        result.push_back(root->val);
        result.insert(result.end(), r.begin(), r.end());

        return result;
    }
};
