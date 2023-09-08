class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        # shorter names and ordered by capacity
        jug1 = min(jug1Capacity, jug2Capacity)
        jug2 = max(jug1Capacity, jug2Capacity)
        target = targetCapacity

        if target > jug1 + jug2:
            return False

        # I had a longer approach with dynamic programming which was too slow ...
        # then I saw that a test case had two large primes
        # obviously two primes have gcd() = 1
        # therefore I digged deeper and discovered this much shorter solution:
        # target must be a multiple of the common factors of jug1 and jug2
        return target % gcd(jug1, jug2) == 0

        # honestly I hate this problem because it isn't about programming but solely about math
