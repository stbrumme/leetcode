class Solution {
public:
    int nextGreaterElement(int n) {
        vector<int> digits;
        while (n > 0)
        {
            digits.push_back(n % 10);
            n /= 10;
        }
        reverse(digits.begin(), digits.end());

        if (!next_permutation(digits.begin(), digits.end()))
            return -1;

        reverse(digits.begin(), digits.end());
        int64_t result = 0;
        while (!digits.empty())
        {
            result *= 10;
            result += digits.back();
            digits.pop_back();
        }

        if (result >= 2147483648)
            return -1;
        return result;
    }
};
