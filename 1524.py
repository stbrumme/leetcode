class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0

        total = 0
        odd   = 0
        even  = 1 # pretend to prepend a zero
        for a in arr:
            total += a

            if total & 1:
                result += even
                odd    += 1
            else:
                result += odd
                even   += 1

        return result % 1_000_000_007
