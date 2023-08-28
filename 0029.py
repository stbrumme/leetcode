class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = abs(dividend)
        b = abs(divisor)

        c = 0
        shift = 33
        while a > 0 and shift >= 0:
            sub = b << shift
            if a >= sub:
                a -= sub
                c += 1 << shift

            shift -= 1

        if dividend >= 0 and divisor >= 0:
            return min(c, +2147483647)
        if dividend < 0 and divisor < 0:
            return min(c, +2147483647)
        return max(-c, -2147483648)
