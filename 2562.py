class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        while len(nums) >= 2:
            concat  = str(nums[0]) + str(nums[-1])
            result += int(concat)
            nums.pop(0)
            nums.pop()

        return result + nums[0] if nums else result
