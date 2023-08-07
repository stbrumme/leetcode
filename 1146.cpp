class SnapshotArray {
    vector<vector<int>> when;
    vector<vector<int>> what;
    int timestamp;

public:
    SnapshotArray(int length) {
        when.resize(length);
        what.resize(length);
        timestamp = 0;
    }

    void set(int index, int val) {
        when[index].push_back(timestamp);
        what[index].push_back(val);
    }

    int snap() {
        return timestamp++;
    }

    int get(int index, int snap_id) {
        auto& bucket = when[index];
        auto i = upper_bound(bucket.begin(), bucket.end(), snap_id);

        if (i == bucket.begin())
            return 0;

        i--;
        auto pos = i - bucket.begin();
        return what[index][pos];
    }
};
