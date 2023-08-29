class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [ 0 ] * len(nums)
        combos = [ 0 ] * len(nums)

        for i in range(len(nums)):
            length[i] = 1
            combos[i] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    longer = length[j] + 1
                    if   length[i] == longer:
                        combos[i] += combos[j]
                    elif length[i] <  longer:
                        length[i] = longer
                        combos[i] = combos[j]

        longest = max(length)
        result = 0
        for i in range(len(combos)):
            if length[i] == longest:
                result += combos[i]

        return result
