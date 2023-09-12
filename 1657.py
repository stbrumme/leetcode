class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        def getHistogram(w):
            freq = defaultdict(int)
            for c in w:
                freq[c] += 1
            return freq

        f1 = getHistogram(word1)
        f2 = getHistogram(word2)

        return f1.keys() == f2.keys() and sorted(f1.values()) == sorted(f2.values())
