class Solution:
    def reachNumber(self, target: int) -> int:
        # triangle numbers
        def tri(x):
            return x * (x + 1) // 2

        target = abs(target)
        a = floor((target*2)**0.5) - 1
        while tri(a) < target:
            a += 1

        while (tri(a) - target) % 2 == 1:
            a += 1
        return a