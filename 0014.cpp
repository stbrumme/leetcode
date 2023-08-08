class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int result = 0;
        while (true)
        {
            bool ok = true;
            for (auto& s : strs)
                if (s.size() < result ||
                    s[result] != strs[0][result])
                {
                    ok = false;
                    break;
                }

            if (!ok)
                break;

            result++;
        }

        return strs[0].substr(0, result);
    }
};
