class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        all = None
        for w in words:
            freq = defaultdict(int)
            for c in w:
                freq[c] += 1

            if all:
                for f in all:
                    all[f] = min(all[f], freq[f])
            else:
                all = freq

        for a in all:
            for _ in range(all[a]):
                yield a
