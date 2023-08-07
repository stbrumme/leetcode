class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        map<int, int> lengths;
        for (auto x : nums)
        {
            auto maxx = 0;
            for (auto i = lengths.begin(); i->first < x && i != lengths.end(); i++)
                if (maxx < i->second)
                    maxx = i->second;

            lengths[x] = maxx + 1;
        }

        auto result = 0;
        for (auto l : lengths)
            if (result < l.second)
                result = l.second;

        return result;
    }
};
