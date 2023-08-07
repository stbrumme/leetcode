class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (auto& r : matrix)
        {
            if (target < r.front())
                return false;
            if (target > r.back())
                continue;

            return binary_search(r.begin(), r.end(), target);
        }

        return false;
    }
};
