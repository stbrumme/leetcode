class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # [ 1,2,...,1000 ]
        low  =    1
        high = 1000
        all  = list(range(low, high + 1))

        for x in all:
            # no solution for x ? (these checks aren't needed, they just improve performance)
            if customfunction.f(x, low)  > z:
                break
            if customfunction.f(x, high) < z:
                continue

            # find lowest y where f(x, y) == z
            left  = bisect_left(all, z,     key = lambda y, x=x : customfunction.f(x, y))
            # find lowest y where f(x, y) > z
            right = bisect_left(all, z + 1, key = lambda y, x=x : customfunction.f(x, y))
            # linear scan until f(x, y) becomes too large
            for y in range(all[left], all[right]):
                yield [ x, y ]
