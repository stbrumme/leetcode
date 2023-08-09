class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        map<int, int> freq;
        for (int i = 0; i < k; i++)
            freq[nums[i]]++;

        vector<int> result;
        result.push_back(freq.rbegin()->first);

        for (int i = 1; i <= nums.size() - k; i++)
        {
            auto prev = nums[i - 1];
            auto next = nums[i - 1 + k];

            freq[prev]--;
            freq[next]++;

            auto top = freq.rbegin()->first;
            if (prev == top)
                while (!freq.empty() && freq[top] == 0)
                {
                    freq.erase(top);
                    top = freq.rbegin()->first;
                }

            result.push_back(top);
        }

        return result;
    }
};
