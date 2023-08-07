class Solution {
    map<pair<int,int>, int> cache;
    int dp(const vector<vector<int>>& tri, int r, int c)
    {
        if (r == tri.size())
            return 0;

        auto lookup = cache.find({r,c});
        if (lookup != cache.end())
            return lookup->second;

        int a = tri[r][c] + dp(tri, r+1, c);
        int b = tri[r][c] + dp(tri, r+1, c+1);
        int result = a < b ? a : b;
        cache[{r,c}] = result;
        return result;
    }

public:
    int minimumTotal(vector<vector<int>>& triangle) {
        cache.clear();
        return dp(triangle, 0,0);
    }
};
