class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # L blocks R (and vice versa)
        # so that their relative order must be identical
        s = start .replace("_", "")
        t = target.replace("_", "")
        if s != t:
            return False

        left  = 0 # number of L seen in target but not in start
        right = 0 # number of R seen in start  but not in target
        for a, b in zip(start, target):
            if   a == "L":
                left  -= 1
            elif a == "R":
                right += 1

            if   b == "L":
                left  += 1
            elif b == "R":
                right -= 1

            if left < 0 or right < 0:
                return False

        return True
