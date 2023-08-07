class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        // just tired of binary search ...
        if (k < arr[0])
            return k;

        int missing = arr[0] - 1;

        for (int i = 1; i < arr.size(); i++)
        {
            auto gap = arr[i] - arr[i-1] - 1;
            if (missing + gap >= k)
                return arr[i-1] + k - missing;

            missing += gap;
        }

        return arr.back() + k - missing;
    }
};
