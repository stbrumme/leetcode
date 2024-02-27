class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data  = defaultdict(int)  # (key, value)
        self.used  = defaultdict(int)  # (key, numUsed)
        self.freq  = defaultdict(list) # (numUsed, (key1, key2, ...)) keys sorted by age
        self.least = 0                 # min(self.freq)

    # internal function: updates LFU counters, key MUST exist
    def access(self, key):
        # increment usage counter
        previous = self.used[key]
        current  = previous + 1
        self.used[key] = current # or += 1

        # update self.freq
        self.freq[current ].append(key)
        self.freq[previous].remove(key)
        if not self.freq[previous]: # no item left with old count
            self.freq.pop(previous)
            # maybe it was the least frequent item
            if previous == self.least:
                self.least = current # or += 1

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1 # unknown

        self.access(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        # overwrite an existing item
        if key in self.data:
            self.access(key) # update LFU counters
            self.data[key] = value
            return

        # evict an item
        if len(self.data) == self.capacity:
            # remove this key from all data structures
            evict = self.freq[self.least].pop(0)
            if not self.freq[self.least]:
                self.freq.pop(self.least)
            self.used.pop(evict)
            self.data.pop(evict)

        # now there's at least one slot avaiable for this shiny new item
        self.data[key] = value
        self.used[key] = 1
        self.least     = 1
        self.freq[1].append(key)
