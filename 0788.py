class Solution:
    def rotatedDigits(self, n: int) -> int:
        def good(n): # 1 = True, 0 = False
            modified = 0
            for c in str(n):
                # cannot rotate
                if c in [ "3", "4", "7" ]:
                    return 0
                # at least one digit must alter the result
                if c in [ "2", "5", "6", "9" ]:
                    modified = 1

            return modified

        return sum(good(i) for i in range(1, n + 1))
