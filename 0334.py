class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = nums[0]
        two = float("+inf")

        for n in nums:
            if n > two:
                return True

            if n <= one:
                one = n
            elif n < two:
                two = n

        return False
