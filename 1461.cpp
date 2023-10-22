class Solution {
public:
    bool hasAllCodes(string s, int k)
    {
        // too short
        if (s.size() <= k)
            return false;

        vector<bool> have(1 << k, false);
        int mask = (1 << k) - 1;
        int bits = 0;
        // build initial code of length k - 1
        for (int i = 0; i < k - 1; i++)
        {
            bits <<= 1;
            bits  |= s[i] - '0';
        }

        // add all codes with length k
        for (int i = k - 1; i < s.size(); i++)
        {
            bits <<= 1;
            bits  &= mask;
            bits  |= s[i] - '0';
            have[bits] = true;
        }

        // if all codes of length k are found, then all codes of small length are part of s, too
        for (int i = 0; i < have.size(); i++)
            if (!have[i])
                return false;
        return true;
    }
};
