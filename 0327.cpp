class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int result = 0;

        // map is too slow, therefore two passes:
        // 1. find all unique sums, sort them
        // 2. compute frequency of each sum using binary search in a vector

        vector<int64_t> sums;
        int64_t sum = 0;
        for (auto n : nums)
        {
            sum += n;
            sums.push_back(sum);
        }

        sort(sums.begin(), sums.end());
        auto last = unique(sums.begin(), sums.end());
        sums.resize(distance(sums.begin(), last));
        // now we know the unique sums

        sum = 0;
        vector<int> count(sums.size(), 0);
        for (auto n : nums)
        {
            sum += n;

            // from beginning
            if (sum >= lower && sum <= upper)
                result++;

            // starts somehwhere in the middle, runs until current element
            auto a = distance(sums.begin(), lower_bound(sums.begin(), sums.end(), sum - upper));
            auto b = distance(sums.begin(), upper_bound(sums.begin(), sums.end(), sum - lower));
            for (; a != b; a++)
                result += count[a];

            auto current = distance(sums.begin(), lower_bound(sums.begin(), sums.end(), sum));
            count[current]++;
        }

        return result;
    }
};
