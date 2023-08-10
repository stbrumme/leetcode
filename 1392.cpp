class Solution {
    typedef uint8_t hashsize;
    hashsize hash(array<uint32_t, 26>& f)
    {
        hashsize result = 0;
        for (auto x : f)
            result = hashsize(result * 7) ^ x;
        return result;
    }

public:
    string longestPrefix(string s) {
        vector<hashsize> fingerprints(s.size());

        array<uint32_t, 26> current = { 0 };
        for (int i = s.size() - 1; i >= 0; i--)
        {
            current[s[i] - 'a']++;
            fingerprints[i] = hash(current);
        }

        for (int length = s.size() - 1; length > 0; length--)
        {
            current[s[length] - 'a']--;

            int start = s.size() - length;
            if (hash(current) != fingerprints[start])
                continue;

            bool ok = true;
            for (int i = 0; i < length; i++)
                if (s[i] != s[i + start])
                {
                    ok = false;
                    break;
                }

            if (ok)
                return s.substr(0, length);
        }

        return "";
    }
};
