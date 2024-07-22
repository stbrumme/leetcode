class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        # (a AND b) <= a as well as (a AND b) <= b
        # therefore subarrays' AND value becomes smaller and smaller

        have   = defaultdict(int) # ANDed value => number of subarrays
        for n in nums:
            next = defaultdict(int)

            for h, count in have.items():
                longer = h & n
                if longer >= k: # reject if < k
                    next[longer] += count

            if n >= k:
                next[n] += 1

            have    = next
            result += have[k]

        return result
