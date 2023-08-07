class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        // x = a + b*n
        sort(arr.begin(), arr.end());
        auto diff = arr[1] - arr[0];
        for (auto i = 2; i < arr.size(); i++)
            if (arr[i] - arr[i-1] != diff)
                return false;

        return true;
    }
};
