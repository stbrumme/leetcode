class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        @cache
        def deeper(last, z, o): # z and o stand for the numbers of remaining zeros or ones
            if z == 0 or o == 0:
                return z + o <= limit

            # repeat the last symbol once more or switch to the other symbol
            result = 0
            if last != 0:
                for i in range(1, min(z, limit) + 1):
                    result += deeper(0, z - i, o)
            if last != 1:
                for i in range(1, min(o, limit) + 1):
                    result += deeper(1, z, o - i)

            return result % 1_000_000_007

        return deeper(2, zero, one) # 2 is a placeholder to indicate "doesn't matter whether strings start with 0 and 1
