class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        size = len(nums)

        # this problem relies on a non-standard definition of "median":
        # it's always a number of the subarray, never (a+b)/2 for even arrays

        # each subarray with median k must contain k, too
        # hence they start before/at "mid" and end after/at "mid"
        mid = nums.index(k)

        # beginning from mid, count smaller and larger numbers
        smaller = [ 0 ] * size
        larger  = [ 0 ] * size
        # count to the left
        for i in reversed(range(mid)):
            smaller[i] = smaller[i + 1] + (nums[i] < k)
            larger [i] = larger [i + 1] + (nums[i] > k)
            delta = larger[i] - smaller[i]
        # count to the right
        for i in range(mid + 1, size):
            smaller[i] = smaller[i - 1] + (nums[i] < k)
            larger [i] = larger [i - 1] + (nums[i] > k)

        left  = defaultdict(int) # frequency of larger[i] - smaller[i] on left  side of k
        for i in range(mid + 1):
            left [larger[i] - smaller[i]] += 1
        right = defaultdict(int) # frequency of larger[i] - smaller[i] on right side of k
        for i in range(mid, size):
            right[larger[i] - smaller[i]] += 1

        for delta in left:
            # odd  length, both deltas must add to zero
            if -delta     in right:
                result += left[delta] * right[-delta]

            # even length, both deltas must add to zero
            if -delta + 1 in right:
                result += left[delta] * right[-delta + 1]

        return result
