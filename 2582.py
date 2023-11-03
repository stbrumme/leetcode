class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # let's simulate it and avoid modulo arithmetic
        pos = 1
        dir = +1
        for i in range(time):
            if pos == n:
                dir = -1
            if pos == 1:
                dir = +1

            pos += dir

        return pos
