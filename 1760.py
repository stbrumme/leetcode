class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # steps required to split each bag such that it fits the maximum size
        def steps(size):
            result = 0
            for n in nums:
                if n > size:
                    # break down each oversized bag into bags of size "size"
                    smaller = ceil(n / size)
                    result += smaller - 1
            return result

        left  = 1
        right = max(nums)
        while left != right:
            mid = (left + right) // 2
            if steps(mid) > maxOperations:
                left  = mid + 1
            else:
                right = mid

        return left
