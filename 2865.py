class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        result = 0

        # brute force
        for i, m in enumerate(maxHeights):
            total = 0

            # scan left
            height = m
            for j in reversed(range(i)):
                height = min(height, maxHeights[j])
                total += height

            # scan right
            height = m
            for j in range(i, len(maxHeights)):
                height = min(height, maxHeights[j])
                total += height

            result = max(result, total)

        return result
