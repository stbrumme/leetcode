class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # "constant extra space" => let's have always 10^5 extra space
        count = [ 0 ] * 100001
        for n in nums:
            count[n] += 1
            if count[n] > 1:
                yield n
