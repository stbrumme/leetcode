class DataStream:
    def __init__(self, value: int, k: int):
        self.all   = []
        self.freq  = defaultdict(int)

        self.value = value
        self.k     = k

    def consec(self, num: int) -> bool:
        self.freq[num] += 1
        self.all.append(num)

        # remove old entries
        if len(self.all) > self.k:
            slideout = self.all[-self.k - 1]
            if self.freq[slideout] == 1:
                del self.freq[slideout]
            else:
                self.freq[slideout] -= 1

        return num == self.value and self.freq[num] == self.k
