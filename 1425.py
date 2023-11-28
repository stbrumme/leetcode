class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        best = [ 0 ] # descending order of best recent indices
        high = [ nums[0] ]
        for i, n in enumerate(nums):
            if i == 0:
                continue

            high.append(max(n, high[best[0]] + n))

            # remove worse choices
            while best and high[best[-1]] < high[-1]:
                best.pop()
            # remove outdated
            if best and best[0] + k <= i:
                best.pop(0)

            best.append(i)

        return max(high)
