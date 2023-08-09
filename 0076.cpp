class Solution {
public:
    string minWindow(string s, string t) {
        int need[256] = { 0 };
        for (auto c : t)
            need[c]++;

        int have[256] = { 0 };
        string result;

        int left = 0;
        for (int right = 0; right < s.size(); right++)
        {
            // append
            auto current = s[right];
            have[current]++;

            // shrink
            while (left < right)
            {
                auto l = s[left];

                if (need[l] >= have[l])
                    break;

                left++;
                have[l]--;
            }

            // match ?
            bool ok = true;
            for (char c = 'A'; c <= 'z'; c++)
                ok &= need[c] <= have[c];

            if (!ok)
                continue;

            auto length = right - left + 1;
            if (result.empty() || length < result.size())
                result = s.substr(left, length);
        }

        return result;
    }
};
