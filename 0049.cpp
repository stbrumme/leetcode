class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (auto& s : strs)
        {
            auto original = s;
            sort(s.begin(), s.end());
            groups[s].push_back(original);
        }

        vector<vector<string>> result;
        for (auto& g : groups)
            result.emplace_back(g.second);
        return result;
    }
};
