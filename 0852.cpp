class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        // brute-force
        auto i = max_element(arr.begin(), arr.end());
        return i - arr.begin();
    }
};
