class Solution {
public:
    int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
        // plant longest growing first
        vector<pair<int, int>> all; // growTime => plantTime
        all.reserve(plantTime.size());
        for (int i = 0; i < plantTime.size(); i++)
            all.push_back({ growTime[i], plantTime[i] });

        sort(all.rbegin(), all.rend());

        int plantDays = 0;
        int latest = 0;
        for (auto i : all)
        {
            plantDays += i.second;
            int bloom = plantDays + i.first;
            latest = max(latest, bloom);
        }

        return latest;
    }
};
