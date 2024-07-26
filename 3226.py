class Solution:
    def minChanges(self, n: int, k: int) -> int:
        result = 0
        while n or k:
            have = n & 1
            need = k & 1
            if have != need:
                if need:
                    return -1
                else:
                    result += 1

            n >>= 1
            k >>= 1

        return result
