class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # need an even number of chairs
        n = corridor.count("S")
        if n == 0 or n & 1:
            return 0

        result = 1
        modulo = 1_000_000_007
        plants = 0 # plants between each second and third chair
        seats  = 0 # reset once we reached the third chair
        for c in corridor:
            if c == "S":
                seats += 1
                if seats == 3:
                    result *= plants + 1
                    result %= modulo
                    seats  = 1
                    plants = 0
            else:
                if seats == 2:
                    plants += 1

        return result
