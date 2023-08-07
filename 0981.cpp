class TimeMap {
    unordered_map<string, map<int, string>> data;

public:
    void set(string key, string value, int timestamp) {
        data[key][timestamp] = value;
    }

    string get(string key, int timestamp) {
        auto slot = data.find(key);
        if (slot == data.end())
            return "";

        auto& bucket = slot->second;

        auto pos = bucket.upper_bound(timestamp);
        if (pos == bucket.begin())
            return "";

        pos--;
        return pos->second;
    }
};
