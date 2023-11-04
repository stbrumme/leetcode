class Solution:
    def maxScore(self, nums: List[int]) -> int:
        size = len(nums)

        # bitmask
        all = (1 << size) - 1

        # precompute GCDs
        g = []
        for a in range(size):
            g.append([])
            for b in range(size):
                g[-1].append(gcd(nums[a], nums[b]))

        @cache
        def deeper(picked):
            if picked == all:
                return 0

            best   = 0
            factor = (picked.bit_count() // 2) + 1

            for a in range(size):
                maska = 1 << a
                if picked & maska:
                    continue

                for b in range(a + 1, size):
                    maskb = 1 << b
                    if picked & maskb:
                        continue

                    current = factor * g[a][b]
                    next = picked | maska | maskb
                    best = max(best, current + deeper(next))

            return best

        return deeper(0)
