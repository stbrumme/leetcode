class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # don't move => ping-pong or triangle move
        if sx == fx and sy == fy:
            return t != 1 # impossible with only one move

        # shortest route
        distance = max(abs(sx - fx), abs(sy - fy))
        return distance <= t
