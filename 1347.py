class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqS = defaultdict(int)
        for c in s:
            freqS[c] += 1

        freqT = defaultdict(int)
        for c in t:
            freqT[c] += 1

        result = 0
        for f in freqS:
            if freqS[f] > freqT[f]:
                result += freqS[f] - freqT[f]

        return result
