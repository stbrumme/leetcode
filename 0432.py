class AllOne:
    def __init__(self):
        self.count   = { }              # each key and its count
        self.classes = defaultdict(set) # classes[i] contains all keys with count i
        self.high = 0                   # highest count
        self.low  = 0                   # lowest count

    def inc(self, key: str) -> None:
        if key in self.count:
            # existing
            count = self.count[key]
            self.classes[count].discard(key)
            self.classes[count + 1].add(key)
            self.count[key] += 1

            if self.high == count:
                self.high += 1
            if self.low  == count and not self.classes[count]:
                self.low  += 1
        else:
            # new key
            self.classes[1].add(key)
            self.count[key] = 1

            if self.high == 0:
                self.high = 1
            self.low  = 1

    def dec(self, key: str) -> None:
        count = self.count[key]
        self.classes[count].discard(key)

        if count > 1:
            self.classes[count - 1].add(key)
            self.count[key] -= 1
        else:
            # remove
            self.classes[1].discard(key)
            del self.count[key]

        if self.high == count and not self.classes[count]:
            self.high -= 1
        if self.low  == count:
            self.low  -= 1
            if self.low == 0:
                # strictly speaking not O(1)
                if self.count:
                    self.low = 1
                    while not self.classes[self.low]:
                        self.low += 1

    def getMaxKey(self) -> str:
        if self.high == 0 or not self.classes[self.high]:
            return ""
        for x in self.classes[self.high]:
            return x # return first element

    def getMinKey(self) -> str:
        if self.low == 0 or not self.classes[self.low]:
            return ""
        for x in self.classes[self.low]:
            return x # return first element
