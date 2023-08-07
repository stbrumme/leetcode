class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        for (auto stride = 1; stride <= s.size()/2; stride++)
        {
            if (s.size() % stride != 0)
                continue;

            bool ok = true;
            for (auto i = 0; i < stride && ok; i++)
                for (auto j = i + stride; j < s.size() && ok; j += stride)
                    if (s[i] != s[j])
                        ok = false;

            if (ok)
                return true;
        }

        return false;
    }
};
