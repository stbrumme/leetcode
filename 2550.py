class Solution:
    def monkeyMove(self, n: int) -> int:
        # the first 8 test cases reveal it's
        # https://oeis.org/A000918
        modulo = 1_000_000_007
        return (pow(2, n, modulo) - 2) % modulo
