class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        # sum of every partition
        need = total // k
        if max(nums) > need:
            return False

        nums.sort(reverse = True)
        while nums and nums[0] == need:
            nums.pop(0)
            k -= 1
        if k == 0:
            return True

        def deeper(pos, have):
            if pos == len(nums):
                return min(have) == need

            # try to add current number to an existing set
            n = nums[pos]
            for i in range(len(have)):
                have[i] += n
                if have[i] <= need:
                    if deeper(pos + 1, have):
                        return True
                have[i] -= n

            # start new set
            if len(have) == k:
                return False
            return deeper(pos + 1, have + [ n ])

        return deeper(0, [])
