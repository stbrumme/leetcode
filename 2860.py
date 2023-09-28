class Solution:
    def countWays(self, nums: List[int]) -> int:
        all = defaultdict(int)
        for n in nums:
            all[n] += 1

        result = 1 if 0 not in all else 0 # select none

        have = 0
        for i in sorted(all):
            shared = all[i] # students with same threshold

            if i < have + shared:
                result += 1
                for j in range(i + 1, have + shared + 1):
                    if j in all:
                        result -= 1 # undo
                        break

            have += shared

        return result
