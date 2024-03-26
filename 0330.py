class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result = 0

        # each sorted list is a min-heap
        nums.append(n + 1) # avoid an empty heap

        unknown = 1 # next number not yet formed
        while unknown <= n:
            # there is a gap, we can't build number "unknown"
            if nums[0] > unknown:
                # patch that number
                heappush(nums, unknown)
                result += 1

            # we can add nums[0] to all already known numbers and thus extend our range
            unknown += heappop(nums)

        return result
