class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        diff = []
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i - 1])

        result = -1
        for left in range(len(diff)):
            if diff[left] != +1:
                continue
            expect = -1
            length = 2
            for right in range(left + 1, len(diff)):
                if diff[right] != expect:
                    break
                length += 1
                expect = -expect

            result = max(result, length)

        return result
