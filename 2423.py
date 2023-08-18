class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1

        ff = defaultdict(int)
        for f in freq:
            ff[freq[f]] += 1

        high = max(freq.values())
        low  = min(freq.values())

        # single letter
        if len(freq) == 1:
            return True

        # all occur once
        if len(ff) == 1 and high == 1:
            return True

        # remove most frequest
        if len(ff) == 2 and ff[high] == 1 and high == low + 1:
            return True

        # remove least frequest
        if len(ff) == 2 and ff[low] == 1 and low == 1:
            return True

        return False
