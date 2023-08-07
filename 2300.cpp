class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());

        vector<int> result;
        result.reserve(spells.size());
        for (int s : spells)
        {
            auto minPotions = success / s;
            if (success % s != 0)
                minPotions++;

            auto i = lower_bound(potions.begin(), potions.end(), minPotions);
            auto ok = distance(i, potions.end());
            result.push_back(ok);
        }
        return result;
    }
};
