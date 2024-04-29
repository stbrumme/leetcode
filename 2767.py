class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        fives = []
        for i in range(6 + 1): # at most 5^6
            fives.append(bin(5 ** i)[2 :])

        def deeper(text):
            if not text:
                return 0

            best = +inf
            for f in fives:
                if text.startswith(f):
                    best = min(best, 1 + deeper(text[len(f) :]))
            return best

        result = deeper(s)
        return result if result != +inf else -1
