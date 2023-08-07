class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int sum = 0;
        for (int i = 0; i < mat.size(); i++)
        {
            sum += mat[i][i];
            auto j = mat.size() - i - 1;
            if (i != j)
                sum += mat[i][j];
        }
        return sum;
    }
};
