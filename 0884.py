class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq1 = defaultdict(int)
        for w in s1.split(" "):
            freq1[w] += 1

        freq2 = defaultdict(int)
        for w in s2.split(" "):
            freq2[w] += 1

        for f in freq1:
            if freq1[f] == 1 and f not in freq2:
                yield f
        for f in freq2:
            if freq2[f] == 1 and f not in freq1:
                yield f
