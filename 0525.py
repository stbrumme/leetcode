class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = dict()
        first[0] = -1

        result = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current -= 1
            else:
                current += 1
            print(i, "=", current)

            if current in first:
                distance = i - first[current]
                result = max(result, distance)
            else:
                first[current] = i

        return result
