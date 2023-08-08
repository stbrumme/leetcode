class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty())
            return {};

        map<int, set<string>> dp;
        dp[0] = { "" };

        for (int i = 0; i < digits.size(); i++)
        {
            string choice;
            switch (digits[i])
            {
                case '2': choice = "abc"; break;
                case '3': choice = "def"; break;
                case '4': choice = "ghi"; break;
                case '5': choice = "jkl"; break;
                case '6': choice = "mno"; break;
                case '7': choice = "pqrs"; break;
                case '8': choice = "tuv"; break;
                case '9': choice = "wxyz"; break;
            }

            for (auto& prefix : dp[i])
                for (auto c : choice)
                    dp[i+1].insert(prefix + c);
        }

        auto& final = dp[digits.size()];
        return { final.begin(), final.end() };
    }
};

