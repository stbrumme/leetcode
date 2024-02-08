class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # remove all beans on the left side of i, reduce all bags to n beans if on the right side of i
        result = total = sum(beans)
        left   = 0
        for i, b in enumerate(sorted(beans)):
            remaining = len(beans) - i
            left  += b
            right  = total - left - remaining * b
            result = min(result, left + right)

        return result
