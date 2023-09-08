class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        map<int, int> up, down;

        for (auto n : nums)
        {
            if (up.count(n) == 0)
                up[n] = 1;
            if (down.count(n) == 0)
                down[n] = 1;

            for (auto i = down.begin(); i != down.lower_bound(n); i++)
                up[n]   = max(up[n],   i->second + 1);
            for (auto i = up.upper_bound(n); i != up.end(); i++)
                down[n] = max(down[n], i->second + 1);
        }

        int result = 0;
        for (auto i : up)
            result = max(result, i.second);
        for (auto i : down)
            result = max(result, i.second);

        return result;
    }
};
