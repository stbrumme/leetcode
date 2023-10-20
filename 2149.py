class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [] # could be done without extra space, too
        pos = neg = 0
        while len(result) < len(nums):
            while nums[pos] < 0:
                pos += 1
            while nums[neg] > 0:
                neg += 1

            result.append(nums[pos])
            result.append(nums[neg])
            pos += 1
            neg += 1

        return result
