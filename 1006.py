class Solution:
    def clumsy(self, n: int) -> int:
        ops = cycle( [ "*", "//", "+", "-" ] )
        return eval("".join(str(i) + next(ops) for i in range(n, 1, -1)) + "1")
