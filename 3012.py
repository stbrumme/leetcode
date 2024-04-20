class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        # always combine the smallest with all bigger numbers: small % bigger = small
        # in the end only the smallest number is left
        low = min(nums)

        # the smallest numbers can be found in two ways:
        # 1) it can be min(nums)
        # 2) it can be nums[i] % min(nums) if nums[i] is not a multiple of min(nums)
        if low > 1:
            for n in nums:
                if n % low != 0:
                    return 1

        remain = nums.count(low)
        # a % a = 0, which cannot be further reduced
        # so we get  [ 0 ] * (remain // 2)
        # or [ a ] + [ 0 ] * (remain // 2)

        if remain & 1:
            return 1 + remain // 2 # second case
        else:
            return     remain // 2 # first  case
