class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def factor(n):
            high = int(sqrt(n))
            for i in range(high, 0, -1):
                if n % i == 0:
                    return i

        a = factor(num + 1)
        b = (num + 1) // a

        x = factor(num + 2)
        y = (num + 2) // x

        return [ a, b ] if abs(a - b) <= abs(x - y) else [ x, y ]
