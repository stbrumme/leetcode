class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        size  = max(fruits[-1][0], startPos) + 1
        total = [ 0 ] * size # accumulated fruits between here and startPos
        for x, berries in fruits:
            total[x] = berries

        # scan left
        have = 0
        for x in reversed(range(startPos + 1)):
            have += total[x]
            total[x] = have
        # scan right
        have = 0
        for x in range(startPos, size):
            have += total[x]
            total[x] = have

        result = total[startPos]
        # walk to the left, then to the right
        for left in reversed(range(startPos)):
            distance = startPos - left
            if distance > k:
                break

            # pick berries
            result = max(result, total[left])

            walkback = 2 * distance
            if walkback >= k:
                continue

            right = startPos + (k - walkback)
            right = min(right, size - 1)
            result = max(result, total[left] + total[right] - total[startPos])

        # walk to the right, then to the left
        # (basically the same code)
        for right in range(startPos + 1, size):
            distance = right - startPos
            if distance > k:
                break

            # pick berries
            result = max(result, total[right])

            walkback = 2 * distance
            if walkback >= k:
                continue

            left = startPos - (k - walkback)
            left = max(left, 0)
            result = max(result, total[left] + total[right] - total[startPos])

        return result
