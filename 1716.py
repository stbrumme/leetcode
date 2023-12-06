class Solution:
    def totalMoney(self, n: int) -> int:
        # it's too early in the morning to figure out the smart modulo math with triangle numbers,
        # let's just brute force it :-)
        result = 0
        add    = 0
        for i in range(n):
            add    += 1
            result += add
            if i % 7 == 6: # Sunday
                add -= 6

        return result
