class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # count "x", "y"
        x  = s1.count("x") + s2.count("x")
        y  = s1.count("y") + s2.count("y")
        if (x & 1) or (y & 1):
            return -1

        # as well as differences between s1 and s2
        xy = yx = 0
        for a, b in zip(s1, s2):
            if a < b:
                xy += 1
            if a > b:
                yx += 1

        result  = xy // 2
        result += yx // 2
        result += xy & 1
        result += yx & 1
        return result
