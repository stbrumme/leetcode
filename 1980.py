class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        i = 0
        # create numbers 0,1,2,3,... in binary of length n
        while True:
            bits  = bin(i)[2:]
            zeros = "0" * (length - len(bits)) # prepend zeros
            bits  = zeros + bits
            if bits not in nums:
                return bits

            i += 1
