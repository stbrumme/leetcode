class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        for pos in range(n):
            mask = 1 << pos

            # flip bits
            aa   = a ^ mask
            bb   = b ^ mask

            # bigger is better ...
            if a * b < aa * bb:
                a = aa
                b = bb

        return (a * b) % 1_000_000_007
