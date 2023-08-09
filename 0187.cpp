class Solution {
    char hashCode[256];
    int hashDNA(const string& s, int from, int length)
    {
        int result = 0;
        for (int i = 0; i < length; i++)
        {
            auto current = s[from + i];
            result <<= 2;
            result  += hashCode[current];
        }
        return result;
    }

public:
    vector<string> findRepeatedDnaSequences(string s) {
        const int limit = 10;

        hashCode['A'] = 0;
        hashCode['C'] = 1;
        hashCode['G'] = 2;
        hashCode['T'] = 3;

        unordered_map<int, short> freq;
        vector<string> result;
        for (int last = limit; last <= s.size(); last++)
            if (++freq[hashDNA(s, last - limit, limit)] == 2)
                result.push_back(s.substr(last - limit, limit));

        return result;
    }
};
