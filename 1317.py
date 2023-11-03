class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # stupid brute force
        a = int(n)
        while True:
            a -= 1
            b  = n - a
            if "0" not in str(a) and "0" not in str(b):
                return [ a, b ]
