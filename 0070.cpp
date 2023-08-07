class Solution {
    vector<int> cache;
    int dp(int current, int total)
    {
        if (current >  total)
            return 0;
        if (current == total)
            return 1;

        if (cache[current] >= 0)
            return cache[current];

        int one = dp(current + 1, total);
        int two = dp(current + 2, total);
        int result = one + two;

        cache[current] = result;
        return result;
    }

public:
    int climbStairs(int n) {
        cache.clear();
        cache.resize(50, -1);
        return dp(0, n);
    }
};
