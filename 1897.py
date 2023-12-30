class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) <= 1:
            return True

        freq = defaultdict(int)
        for w in words:
            for c in w:
                freq[c] += 1
        return all(f % len(words) == 0 for f in freq.values())
