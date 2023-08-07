class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool more = true;
        for (int i = digits.size() - 1; i >= 0; i--)
        {
            more = false;
            digits[i]++;
            if (digits[i] < 10)
                break;
            more = true;
            digits[i] = 0;
        }

        if (more)
            digits.insert(digits.begin(), 1);

        return digits;
    }
};
