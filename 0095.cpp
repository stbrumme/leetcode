class Solution {
    TreeNode* add(TreeNode* root, int value)
    {
        if (!root)
            return new TreeNode(value);

        if (value < root->val)
            root->left = add(root->left, value);
        else
            root->right = add(root->right, value);
        return root;
    }

    string flatten(TreeNode* root)
    {
        if (!root)
            return "";

        return "L" + flatten(root->left) + "V" + to_string(root->val) + "R" + flatten(root->right);
    }

public:
    vector<TreeNode*> generateTrees(int n) {
        vector<int> nums;
        for (int i = 1; i <= n; i++)
            nums.push_back(i);

        map<string, TreeNode*> trees;
        do
        {
            TreeNode* root = nullptr;
            for (auto n : nums)
                root = add(root, n);

            trees[flatten(root)] = root;
        } while (next_permutation(nums.begin(), nums.end()));

        vector<TreeNode*> result;
        for (auto t : trees)
            result.push_back(t.second);
        return result;
    }
};
