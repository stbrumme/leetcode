class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        modulo = defaultdict(int) # all numbers nums[i] + c * space share the same remainder
        low    = defaultdict(int) # smallest number for each remainder
        for n in sorted(nums):
            remainder = n % space

            modulo [remainder] += 1
            if remainder not in low:
                low[remainder]  = n

        # maximum number of targets
        most = max(modulo.values())
        # choose the smallest
        candidates = [ low[key] for key, value in modulo.items() if value == most ]
        return min(candidates)
