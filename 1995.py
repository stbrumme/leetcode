class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        result = 0

        size   = len(nums)

        # positions of each number
        lookup = defaultdict(list)
        for i, n in enumerate(nums):
            lookup[n].append(i)

        for a in range(size):
            for b in range(a + 1, size):
                for c in range(b + 1, size):
                    total = nums[a] + nums[b] + nums[c]
                    # does such a number exist ?
                    if total in lookup:
                        for l in lookup[total]:
                            if l > c:
                                result += 1

        return result
