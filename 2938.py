class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        black  = 0
        for c in s:
            if c == "0":
                result += black # move white ball to the left of all black balls seen so far
            else:
                black  += 1
        return result
