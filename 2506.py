class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # 26 bits, one for each letter
        def fingerprint(w):
            bitmask = 0
            for c in w:
                bitmask |= 1 << (ord(c) - ord("a"))
            return bitmask

        result = 0
        have = defaultdict(int)
        for w in words:
            f = fingerprint(w)
            result  += have[f]
            have[f] += 1
        return result
