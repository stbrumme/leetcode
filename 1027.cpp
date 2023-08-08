class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        int best = 1;

        unordered_map<int, int> first;
        for (int i = 0; i < nums.size(); i++)
            if (first.count(nums[i]) == 0)
                first[nums[i]] = i;

        for (int step = -500; step <= 500; step++)
        {
            vector<bool> started(1000, false);

            for (int i = 0; i < nums.size(); i++)
            {
                if (started[nums[i]])
                    continue;
                started[nums[i]] = true;

                auto length = 1;
                auto next = nums[i] + step;

                if (first.count(next) == 0)
                    continue;

                int j = i+1;
                if (j < first[next])
                    j = first[next];

                for (; j < nums.size(); j++)
                {
                    if (next == nums[j])
                    {
                        next += step;
                        length++;
                        if (best < length)
                            best = length;

                        if (first.count(next) == 0)
                            continue;
                    }
                }
            }
        }
        return best;
    }
};

