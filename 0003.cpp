class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<bool> have(256, false);
        int left = 0;
        int maxx = 0;

        for (int right = 0; right < s.size(); right++)
        {
            auto current = s[right];

            if (have[current])
            {
                // shrink
                while (s[left] != current)
                    have[s[left++]] = false;
                left++;
            }

            // enlarge
            have[current] = true;
            if (maxx < right - left + 1)
                maxx = right - left + 1;
        }

        return maxx;
    }
};
