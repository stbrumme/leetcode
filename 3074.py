class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        result = 0
        apples = sum(apple)
        for c in sorted(capacity, reverse = True):
            result += 1
            apples -= c
            if apples <= 0:
                return result
