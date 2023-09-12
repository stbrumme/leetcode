class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        vector<vector<string>> result;

        // no trie, just basic binary search
        sort(products.begin(), products.end());

        string lookFor;
        for (auto i : searchWord)
        {
            lookFor += i;
            vector<string> three;
            auto pos = lower_bound(products.begin(), products.end(), lookFor);
            while (pos != products.end() && three.size() < 3)
            {
                auto next = *pos++;
                if (next.find(lookFor) != 0)
                    break;
                three.push_back(next);
            }
            result.push_back(three);
        }

        return result;
    }
};
