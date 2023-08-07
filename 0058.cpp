class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream m;
        m.str(s);
        int result = 0;
        string word;
        while (m >> word)
            result = word.size();

        return result;
    }
};
