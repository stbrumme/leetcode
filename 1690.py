class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        # prefix sum
        prefix = [ 0 ]
        for s in stones:
            prefix.append(prefix[-1] + s)

        # up to one million different parameter => Python's caching has high memory usage
        # therefore I create my own caching
        size  = len(stones)
        cache = []
        for i in range(size):
            cache.append([ -1 ] * i) # left < right, allocate only what we actually need

        def deeper(left, right):
            if left == right:
                return 0

            # lookup previous results
            known = cache[right][left]
            if known > -1:
                return known

            # sum
            total = prefix[right + 1] - prefix[left]

            # remove on the left  side
            one = (total - stones[left ]) - deeper(left + 1, right)
            # remove on the right side
            two = (total - stones[right]) - deeper(left, right - 1)
            # go for the win !
            cache[right][left] = best = max(one, two)
            return best

        return deeper(0, len(stones) - 1)
