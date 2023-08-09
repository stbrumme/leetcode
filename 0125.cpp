class Solution {
public:
    bool isPalindrome(string s) {
        string p;
        for (auto c : s)
        {
            if (c >= 'A' && c <= 'Z')
                p += c - 'A' + 'a';

            if (c >= 'a' && c <= 'z')
                p += c;

            if (c >= '0' && c <= '9')
                p += c;
        }

        string r = p;
        reverse(r.begin(), r.end());

        return p == r;
    }
};
