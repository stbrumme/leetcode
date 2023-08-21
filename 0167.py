class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        left = 0
        right = size - 1
        while left < right:
            need = target - numbers[left]
            right = bisect.bisect_left(numbers, need, left + 1, right)
            if right < size and need == numbers[right]:
                return [ left + 1, right + 1 ]

            left += 1

        return None
