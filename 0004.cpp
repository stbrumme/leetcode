class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> both = nums1;
        both.insert(both.end(), nums2.begin(), nums2.end());
        sort(both.begin(), both.end());

        int mid = both.size() / 2;
        if (both.size() % 2 == 0)
            return (double(both[mid-1]) + both[mid]) / 2;
        else
            return both[mid];
    }
};
