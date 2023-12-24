class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            current = 0
            for j in range(len(arr) - i):
                current += arr[i + j]
                if (j & 1) == 0: # if j is even then the length is odd
                    result += current
        return result
