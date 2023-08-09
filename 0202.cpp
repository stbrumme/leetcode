class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> seen;

        while (seen.count(n) == 0)
        {
            if (n == 1)
                return true;

            seen.insert(n);

            int square = 0;
            while (n > 0)
            {
                int digit = n % 10;
                n /= 10;
                square += digit * digit;
            }
            n = square;

        }

        return false;
    }
};
