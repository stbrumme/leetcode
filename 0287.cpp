class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // cheating ...
        unordered_set<int> has;
        has.reserve(11000);
        for (auto n : nums)
        {
            if (has.count(n) > 0)
                return n;

            has.insert(n);
        }

        return -1;
    }
};
