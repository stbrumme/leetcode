class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        auto left = lower_bound(arr.begin(), arr.end(), x);

        if (left == arr.end())
            left--;

        if (*left != x && left != arr.begin())
        {
            auto prev = left - 1;
            if (x - *prev <= *left - x)
                left = prev;
        }

        auto right = left;

        for (auto need = k - 1; need > 0; need--)
        {
            auto diffLeft  = 9999999;
            auto diffRight = 9999999;

            if (left != arr.begin())
                diffLeft  = x - *(left - 1);
            if (right + 1 != arr.end())
                diffRight = *(right + 1) - x;

            if (diffLeft <= diffRight)
                left--;
            else
                right++;
        }

        return vector<int>(left, right + 1);
    }
};
