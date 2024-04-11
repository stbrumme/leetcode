class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        # process in reverse: go from target to start

        # steps 1 and 2 are the Euclidean Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm
        # which compute the greatest common divisor

        d = gcd(targetX, targetY)

        # steps 3 and 4 can reach 1 if d is a power of two
        # https://graphics.stanford.edu/~seander/bithacks.html#DetermineIfPowerOf2
        return (d & (d - 1)) == 0
