class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        todo = set([ 0 ])
        for n in nums:
            next = set()
            for t in todo:
                next.add(t)
                if 2 * (n + t) == total:
                    return True
                if 2 * (n + t) <  total:
                    next.add(n + t)
            todo = next

        return False
