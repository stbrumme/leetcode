class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        size = len(nums)

        # prefix sum
        prefix = [ 0 ] + list(accumulate(nums))

        # first[i] contains the sum of the first array, starting at i
        first  = []
        for left in range(size - firstLen + 1):
            right = left + firstLen
            first.append(prefix[right] - prefix[left])

        # second[i] contains the sum of the first array, starting at i
        second = []
        for left in range(size - secondLen + 1):
            right = left + secondLen
            second.append(prefix[right] - prefix[left])

        # just brute force
        result = 0
        for left, f in enumerate(first):
            after  = left + firstLen
            before = left - secondLen
            s1 = max(second[: before + 1]) if before >= 0           else 0
            s2 = max(second[after :])  if after  <  len(second) else 0
            result = max(result, f + max(s1, s2))

        return result
