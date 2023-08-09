class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        // track active flips
        deque<int> flips;
        int good = 1;

        // flips after that point lead to impossible configurations
        int threshold = nums.size() - k;

        int result = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            // expired
            if (!flips.empty() && flips.front() == i)
            {
                flips.pop_front();
                good = 1 - good;
            }

            // no flip ?
            if (nums[i] == good)
                continue;

            // too late, impossible
            if (i > threshold)
                return -1;

            // flip
            result++;

            good = 1 - good;
            flips.push_back(i + k);
        }

        return result;
    }
};
