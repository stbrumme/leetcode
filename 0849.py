class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        space = [ 0 ]
        for s in seats:
            if s == 0:
                space[-1] += 1
            else:
                if space[-1] > 0:
                    space.append(0)

        # space[i] must be > 0
        if space[0] == 0:
            space.pop(0)
        if space[-1] == 0:
            space.pop(-1)

        middle = (max(space) + 1) // 2
        left   = space[ 0] if seats[ 0] == 0 else 0
        right  = space[-1] if seats[-1] == 0 else 0
        return max(left, middle, right)
