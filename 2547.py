class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        size = len(nums)

        @cache
        def deeper(pos):
            if pos == size:
                return 0

            seen  = defaultdict(int) # numbers and their count
            score = k

            best = +inf
            for i in range(pos, size):
                n = nums[i]

                seen[n] += 1
                have = seen[n]
                if   have == 2:
                    score += 2
                elif have >  2:
                    score += 1

                best = min(best, score + deeper(i + 1))

            return best

        return deeper(0)
