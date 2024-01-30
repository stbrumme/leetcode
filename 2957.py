class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        result = 0

        skip = False
        prev = +inf
        for c in word:
            c = ord(c)
            if abs(c - prev) <= 1 and not skip:
                result += 1
                skip = True
            else:
                skip = False

            prev = c

        return result
