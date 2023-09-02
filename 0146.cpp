class LRUCache {
    typedef pair<int, int> Item;                  // key, value
    unordered_map<int, list<Item>::iterator> pos; // key => where in lru
    list<Item> lru;                               // ordered by least recent use
    int maxsize;

public:
    LRUCache(int capacity)
    : maxsize(capacity)
    { }

    int get(int key) {
        if (pos.count(key) == 0)
            return -1;

        auto value = pos[key]->second;

        // move to front
        lru.erase(pos[key]);
        lru.push_front({ key, value });
        pos[key] = lru.begin();

        return value;
    }

    void put(int key, int value) {
        if (pos.count(key) == 0)
        {
            // evict
            if (pos.size() == maxsize)
            {
                auto oldest = lru.back().first;
                lru.erase(prev(lru.end()));
                pos.erase(oldest);
            }
        }
        else
            lru.erase(pos[key]);

        // move to front
        lru.push_front({ key, value });
        pos[key] = lru.begin();
    }
};
