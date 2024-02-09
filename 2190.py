class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        follow = defaultdict(int)

        for a, b in zip(nums, nums[1:]):
            if a == key:
                follow[b] += 1

        result = None
        for f in follow:
            if not result or follow[f] > follow[result]:
                result = f
        return result
