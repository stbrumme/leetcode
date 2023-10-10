class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target = [ 0 ] + target + [ 0 ]

        result = 0
        for i in range(1, len(target)):
            diff = target[i] - target[i - 1]
            if diff > 0:
                result += diff

        return result
