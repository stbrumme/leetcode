class Solution:
    def minTimeToType(self, word: str) -> int:
        result = 0

        def distance(a, b):
            a = ord(a)
            b = ord(b)
            diff = abs(a - b)
            return min(diff, 26 - diff)

        prev = "a"
        for c in word:
            result += 1 + distance(c, prev)
            prev    = c

        return result
