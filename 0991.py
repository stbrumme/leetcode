class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # try to make target smaller/equal to startValue
        steps = 0
        while startValue < target:
            steps += 1
            # perform operations in reverse
            if target & 1:
                target  += 1
            else:
                target //= 2

        # the only way to reach smaller numbers is by painfully subtracting 1
        steps += startValue - target
        return steps
