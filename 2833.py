class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count("L")
        r = moves.count("R")
        x = moves.count("_") # replace all by either L or R
        return x + abs(l - r)
