class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        result = 0

        nums.sort()
        greater = nums.copy()
        for n in nums:
            while greater and greater[0] <= n:
                heappop(greater)

            if not greater:
                break

            result += 1
            heappop(greater)

        return result
