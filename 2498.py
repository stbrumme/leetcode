class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # let's assume we have two frogs A and B jumping from left to right,
        # and noone is jumping back, without touching the same stone twice
        # => that's equivalent to the original problem statement

        # whenever there's a stone, the frog further away is allowed to jump
        result = 0

        a = b = 0
        for s in stones:
            if a < b:
                result = max(result, s - a)
                a = s
            else:
                result = max(result, s - b)
                b = s

        return result

        # in the end the frog jumps
        # on all odd  stones from left  to right and
        # on all even stones from right to left
        # (or vica versa, it doesn't matter)
