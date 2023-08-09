class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        vector<int> letters(256, 0);
        for (auto c : magazine)
            letters[c]++;

        for (auto c : ransomNote)
        {
            if (letters[c] == 0)
                return false;

            letters[c]--;
        }

        return true;
    }
};
