class Solution:
    def countAsterisks(self, s: str) -> int:
        result  = 0
        outside = True
        for c in s:
            if c == "|":
                outside = not outside
            elif c == "*" and outside:
                result += 1
        return result
