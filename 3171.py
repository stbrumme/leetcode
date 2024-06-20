class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        result = +inf

        # maintain a sorted list of ORed values of all subarrays
        have = []
        for n in nums:
            # a single value is a subarray, too
            result = min(result, abs(n - k))

            # keep all values less than k
            next = []
            for h in have:
                more = h | n
                if more < k:
                    if not next or next[-1] != more:
                        next.append(more)
                else:
                    # can't get any better, no need to further track these subarrays
                    result = min(result, more - k)

            # compare against largest value smaller than k
            if next:
                result = min(result, k - next[-1])

            # insert current value
            if n < k:
                insort(next, n)

            have = next

        return result
