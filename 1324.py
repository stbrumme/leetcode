class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        longest = 0
        for w in words:
            longest = max(longest, len(w))

        result = [ "" ] * longest
        for w in words:
            w += " " * (longest - len(w)) # all words will have same size
            for i, c in enumerate(w):
                result[i] += c

        for r in result:
            yield r.rstrip()