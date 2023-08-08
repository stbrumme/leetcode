class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        if (s.size() < p.size())
            return {};
        vector<int> result;

        vector<short> hp(32, 0);
        for (auto c : p)
            hp[c - 'a']++;


        vector<short> h2(32, 0);
        for (int i = 0; i < p.size(); i++)
            h2[s[i] - 'a']++;

        if (hp == h2)
            result.push_back(0);

        for (int i = 1; i + p.size() <= s.size(); i++)
        {
            auto remove = s[i - 1];
            h2[remove - 'a']--;

            h2[s[i + p.size() - 1] - 'a']++;

            if (hp == h2)
                result.push_back(i);
        }

        return result;
    }
};
