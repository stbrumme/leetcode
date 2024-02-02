class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        result = []
        for i, n in enumerate(sorted(nums)):
            # new group of three
            if not result or len(result[-1]) == 3:
                result.append([])

            # extend current group
            result[-1].append(n)
            if max(result[-1]) - min(result[-1]) > k:
                return []

        return result
