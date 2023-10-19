class NumberContainers:
    def __init__(self):
        self.nums  = defaultdict(set) # number   => positions
        self.data  = {}               # position => number
        self.first = {}               # first[x] = min(nums[x])

    def change(self, index: int, number: int) -> None:
        # replace
        if index in self.data:
            # clean up old entry
            old = self.data[index]
            self.nums[old].discard(index)
            # update self.first
            if self.first[old] == index:
                if self.nums[old]:
                    self.first[old] = min(self.nums[old])
                else:
                    del self.first[old]


        # overwrite / insert
        self.data[index] = number
        self.nums[number].add(index)
        if number in self.first:
            self.first[number] = min(self.first[number], index)
        else:
            self.first[number] = index

    def find(self, number: int) -> int:
        return self.first[number] if number in self.first else -1
