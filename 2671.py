class FrequencyTracker:
    def __init__(self):
        self.count = defaultdict(int)
        self.freq  = defaultdict(int)

    def add(self, number: int) -> None:
        before = self.count[number]
        self.count[number] += 1
        after  = self.count[number]

        self.freq[before] -= 1
        self.freq[after]  += 1

    def deleteOne(self, number: int) -> None:
        before = self.count[number]
        if before == 0:
            return
        self.count[number] -= 1
        after  = self.count[number]

        self.freq[before] -= 1
        self.freq[after]  += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq and self.freq[frequency] > 0
