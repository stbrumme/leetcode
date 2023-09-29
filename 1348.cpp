class TweetCounts {
    map<string, map<int, int>> tweets;

public:
    void recordTweet(string tweetName, int time) {
        tweets[tweetName][time]++;
    }

    vector<int> getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime) {
        auto increment = 60;
        if (freq == "hour")
            increment = 60*60;
        if (freq == "day")
            increment = 24*60*60;

        auto& times = tweets[tweetName];
        vector<int> result;
        for (auto current = startTime; current <= endTime; current += increment)
        {
            auto next = min(current + increment - 1, endTime);
            auto from = times.lower_bound(current);
            auto to   = times.upper_bound(next);

            auto count = 0;
            for (auto scan = from; scan != to; scan++)
                count += scan->second;
            result.push_back(count);
        }

        return result;
    }
};
