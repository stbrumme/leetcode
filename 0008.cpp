class Solution {
public:
    int myAtoi(string s) {
        while (!s.empty() && s[0] == ' ')
            s.erase(s.begin());

        if (s.empty())
            return 0;

        bool isNeg = false;
        if (s[0] == '+')
        {
            s.erase(s.begin());
        }
        else if (s[0] == '-')
        {
            isNeg = true;
            s.erase(s.begin());
        }

        int64_t x = 0;
        while (!s.empty() && s[0] >= '0' && s[0] <= '9')
        {
            auto digit = s[0] - '0';
            s.erase(s.begin());

            x = x*10 + digit;

            if (x > std::numeric_limits<int>::max())
                break;
        }

        if (isNeg)
        {
            x = -x;
            x = max<int64_t>(std::numeric_limits<int>::min(), x);
        }
        else
        {
            x = min<int64_t>(std::numeric_limits<int>::max(), x);
        }

        return x;
    }
};
