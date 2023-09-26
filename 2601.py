class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # process in reverse
        for i in range(len(nums) - 2, -1, -1):
            # ok
            if nums[i + 1] > nums[i]:
                continue

            # find smallest prime such that nums[i] < nums[i+1]
            diff = nums[i] - nums[i + 1]
            adjusted = False
            for p in range(max(2, diff + 1), nums[i]):
                isprime = True
                # prime check
                for j in range(2, p):
                    if j * j > p:
                        break
                    if p % j == 0:
                        isprime = False
                        break

                # subtract
                if isprime:
                    adjusted = True
                    nums[i] -= p
                    break

            # no such prime found
            if not adjusted:
                return False

        return True
