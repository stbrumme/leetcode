class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = []

        size = len(rains)
        last = {} # last time it rains over that lake
        next = [ size ] * size # if rains[i] = x then next[i] is the next time
                               # it rains over the same lake

        # look at rainy days
        for i, r in enumerate(rains):
            if r > 0:
                # upcoming rain
                if r in last:
                    next[last[r]] = i
                # past rain
                last[r] = i

        dry = [] # min-heap of lakes that need to be dry by a certain day
        for i, (r, n) in enumerate(zip(rains, next)):
            if r == 0:
                if dry:
                    day, lake = heappop(dry)
                    result.append(lake) # dry a lake
                else:
                    result.append(1)    # no full lakes left, don't do anything (a test case expects 1, though)
            else:
                if dry and dry[0][0] <= i:
                    # missed a deadline, there will be a flood
                    return []

                # next day it rains over the same lake
                if n < size:
                    heappush(dry, ( n, r ))
                result.append(-1)

        return result
