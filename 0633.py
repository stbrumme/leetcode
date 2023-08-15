class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        all = set()

        i = 0
        while i*i <= c:
            if c == i*i:
                return True

            all.add(i*i)
            i += 1

        for squares in all:
            if (c - squares) in all:
                return True

        return False
