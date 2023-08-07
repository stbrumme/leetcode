class Solution {
public:
    int countOdds(int low, int high) {
        if (low == high)
            return low & 1;

        auto result = 0;
        if (low & 1)
        {
            low++;
            result++;
        }
        if (high & 1)
        {
            high--;
            result++;
        }
        return result + (high - low) / 2;
    }
};
