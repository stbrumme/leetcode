class Solution:
    def addMinimum(self, word: str) -> int:
        result = 0
        prev   = ord("c")
        for x in word + "a":
            x = ord(x)
            diff = (x - prev + 2) % 3
            result += diff
            prev = x
        return result
