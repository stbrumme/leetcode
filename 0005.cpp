class Solution {
public:
    string longestPalindrome(string s) {
        string result;
        result += s[0];

        for (int i = 0; i < s.size(); i++)
        {
            // odd
            for (int step = 1; ; step++)
            {
                int left  = i - step;
                int right = i + step;

                if (left < 0 || right == s.size())
                    break;

                if (s[left] != s[right])
                    break;

                if (right - left + 1 > result.size())
                    result = string(s.begin() + left, s.begin() + right + 1);
            }
            // even
            for (int step = 1; ; step++)
            {
                int left  = i - step + 1;
                int right = i + step;

                if (left < 0 || right == s.size())
                    break;

                if (s[left] != s[right])
                    break;

                if (right - left + 1 > result.size())
                    result = string(s.begin() + left, s.begin() + right + 1);
            }
        }

        return result;
    }
};

