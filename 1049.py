class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        result = +inf

        # partition stones into two groups
        # which have (almost) the same weight
        # the weight difference is the final result

        stones.sort(reverse = True) # search should abort earlier
        total  = sum(stones)
        size   = len(stones)

        @cache
        def deeper(pos, weight):
            if pos == size:
                return

            nonlocal result
            if result == 0: # already found perfect match
                return

            # weight difference
            other  = total - weight
            diff   = abs(weight - other)
            result = min(result, diff)

            # keep going
            if weight < other:
                deeper(pos + 1, weight)               # push current stone to other group
                deeper(pos + 1, weight + stones[pos]) # include stone in our group

        deeper(0, 0)
        return result
