class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # trivial case
        if max(nums) >= k:
            return 1

        result = +inf

        have = {}
        for n in nums:
            next = {}

            for h, length in have.items():
                # one more
                length += 1
                more    = h | n

                if more >= k:
                    # large enough
                    result = min(result, length)

                    # early exit
                    if result == 2:
                        break
                else:
                    # extend array, avoid collisions with shorter arrays
                    next[more] = min(next.get(more, length), length)

            have = next
            have[n] = 1 # start new subarray

        return result if result < +inf else -1
