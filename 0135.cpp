class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies(ratings.size(), 1);

        // left kid
        for (int i = 1; i < ratings.size(); i++)
            if (ratings[i] > ratings[i-1])
                candies[i] = candies[i-1]+1;

        // right kid
        for (int i = ratings.size() - 2; i >= 0; i--)
            if (ratings[i] > ratings[i+1])
                candies[i] = max(candies[i], candies[i+1]+1);

        int result = 0;
        for (auto c : candies)
            result += c;
        return result;
    }
};
