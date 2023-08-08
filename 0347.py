class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        for (auto x : nums)
            freq[x]++;

        multimap<int, int> rev;
        for (auto f : freq)
            rev.insert({ f.second, f.first });

        vector<int> result;
        auto i = rev.rbegin();
        while (k > 0)
        {
            result.push_back(i->second);
            i++;
            k--;
        }
        return result;
    }
};
