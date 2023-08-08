class Solution {
    struct hashPair
    {
        template <typename T, typename U>
        size_t operator()(const std::pair<T, U> &x) const
        {
            return std::hash<T>()(x.first) ^ std::hash<U>()(x.second);
        }
    };

public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<pair<int, int>> data;
        data.reserve(strs.size());
        for (auto& s : strs)
        {
            int one  = 0;
            int zero = 0;
            for (auto c : s)
                if (c == '0')
                    zero++;
                else
                    one++;

            data.push_back({ zero, one });
        }

        map<pair<int, int>, int> dp;
        dp[{ 0, 0 }] = 0;

        int maxx = 0;

        int iteration = 0;
        unordered_map<pair<int, int>, int, hashPair> next;
        for (auto x : data)
        {
            iteration++;

            int left = strs.size() - iteration;

            for (auto i : dp)
            {
                auto key   = i.first;
                auto depth = i.second + 1;

                // can't be better ?
                if (maxx > depth + left)
                    continue;

                auto mm = x.first  + key.first;
                auto nn = x.second + key.second;
                if (mm > m)
                    continue;
                if (nn > n)
                    continue;

                next[{ mm, nn }] = max(dp[{ mm, nn }], depth);

                if (maxx < depth)
                    maxx = depth;
            }

            for (auto i : next)
                dp[i.first] = i.second;
            next.clear();
        }

        return maxx;
    }
};

