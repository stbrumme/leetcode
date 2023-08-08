class Solution {
public:
    int reverse(int x) {
        if (x == 0)
            return 0;

        // cheating by using double instead of int64 (ca. 52 bits)

        bool isNeg = x < 0;
        unsigned int n;
        if (isNeg)
            n = -double(x);
        else
            n = +double(x);

        double result = 0;
        while (n > 0)
        {
            auto digit = n % 10;
            n /= 10;
            result = result * 10 + digit;
        }

        if (result > INT_MAX)
            return 0;
        return isNeg ? -result : +result;
    }
};
