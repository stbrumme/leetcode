class Trie {
    set<string> all;

    // not a trie, just basic tree ...

public:
    void insert(string word) {
        all.insert(word);
    }

    bool search(string word) {
        return all.count(word) > 0;
    }

    bool startsWith(string prefix) {
        auto pos = all.lower_bound(prefix);
        if (pos == all.end())
            return false;

        return pos->find(prefix) == 0;
    }
};
