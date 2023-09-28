class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums.sort()

        k = None
        for i in range(size):
            if k:
                break

            for j in range(i + 1, size):
                delta = nums[j] - nums[i]
                if delta % 2 == 1:
                    continue

                have = nums.copy()
                for i in range(len(have)):
                    if have[i] == 0:
                        continue

                    pos = bisect_left(have, have[i] + delta, i + 1)
                    if pos == len(have) or have[pos] != have[i] + delta:
                        break

                    have[i] = have[pos] = 0

                if sum(have) == 0:
                    k = delta // 2
                    break

        result = []
        have = nums.copy()
        for i in range(len(have)):
            if have[i] == 0:
                continue

            pos = bisect_left(have, have[i] + 2*k, i + 1)
            have[pos] = 0

            result.append(have[i] + k)

        return result
