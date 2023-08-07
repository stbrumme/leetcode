class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        auto i = upper_bound(letters.begin(), letters.end(), target);
        if (i == letters.end())
            return letters[0];

        return *i;
    }
};
