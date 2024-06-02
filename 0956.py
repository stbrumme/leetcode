class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        rods.sort(reverse = True)
        size = len(rods)
        half = sum(rods) // 2 # maximum height

        # total length of remaining rods
        remaining = [ sum(rods[i : ]) for i in range(size) ]

        # second rod
        @cache
        def two(pos, have, need, used):
            if have == need:
                return True  # yes, second rod with identical height found
            if have >  need or pos == size:
                return False

            # not enough rods left
            if have + remaining[pos] < need:
                return False

            # rod not available anymore
            if used & (1 << pos):
                return two(pos + 1, have, need, used)

            # skip rod (and all rods with the same length)
            next = pos + 1
            while next < size and rods[next] == rods[pos]:
                next += 1
            if two(next, have, need, used):
                return True

            # use  rod
            return two(pos + 1, have + rods[pos], need, used)


        # first rod
        @cache
        def one(pos, have, need, used):
            if have == need: # we have our first rod, find second rod with same length
                return two(0, 0, need, used)
            if have >  need or pos == size:
                return False

            # not enough rods left
            if have + remaining[pos] < need:
                return False

            # skip rod (and all rods with the same length)
            next = pos + 1
            while next < size and rods[next] == rods[pos]:
                next += 1
            if one(next, have, need, used):
                return True

            # use  rod
            return one(pos + 1, have + rods[pos], need, used | (1 << pos))

        # try all rod heights, start with the highest
        for length in range(half, 0, -1):
            if one(0, 0, length, 0):
                return length
            one.cache_clear()
            two.cache_clear()

        return 0 # failed
