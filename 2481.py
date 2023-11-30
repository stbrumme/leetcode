class Solution:
    def numberOfCuts(self, n: int) -> int:
        #if n == 1:
        #    return 0
        #return n // 2 if n % 2 == 0 else n

        # let's use the most cryptic bit math, branchfree of course
        return (not (not (n - 1))) * (n >> (1 ^ (n & 1))) # div by 2 if even else 1
