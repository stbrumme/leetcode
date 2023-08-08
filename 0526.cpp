class Solution {
    struct hasher
    {
        template <typename T, typename U>
        size_t operator()(const std::pair<T, U> &x) const
        {
            return std::hash<T>()(x.first) ^ std::hash<U>()(x.second);
        }
    };
    unordered_map<pair<int, int>, int, hasher> cache;

    bool beauty[16][16];

    int dp(int pos, int maxPos, int mask)
    {
        if (pos == maxPos + 1)
            return 1;

        auto key = make_pair(pos, mask);
        auto lookup = cache.find(key);
        if (lookup != cache.end())
            return lookup->second;

        int result = 0;
        for (int bit = 1; bit <= maxPos; bit++)
        {
            int compare = 1 << (bit - 1);
            if ((mask & compare) == 0)
                continue;

            if (!beauty[bit][pos])
                continue;

            result += dp(pos+1, maxPos, mask & ~compare);
        }

        cache[key] = result;
        return result;
    }

public:
    int countArrangement(int n) {
        cache.reserve(20000);

        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                beauty[i][j] = (i % j == 0) || (j % i == 0);

        auto mask = (1 << n) - 1;
        auto result = dp(1, n, mask);

        return result;
    }
};
