class Solution {
public:
    string shortestPalindrome(string s) {
        auto r = s;
        reverse(r.begin(), r.end());

        for (int skip = 0; skip < r.size(); skip++)
        {
            int length = s.size() - skip;
            // check last
            if (r[length - 1 + skip] != s[length - 1])
                continue;

            bool ok = true;

            int steps[] = { 111, 50, 7, 1 };
            for (auto offset : steps)
            {
                if (offset > length)
                    continue;

                for (int i = 0; i < length; i += offset)
                {
                    if (r[i + skip] != s[i])
                    {
                        ok = false;
                        break;
                    }
                }

                if (!ok)
                    break;
            }

            // found it
            if (ok)
            {
                while (skip-- > 0)
                    r += r[skip];
                return r;
            }
        }
        return "";
    }
};
