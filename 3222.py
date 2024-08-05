class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        result = 0 # alternate between 0 = Alice, 1 = Bob

        # 110 = 75 + 4 * 10
        while x >= 0 and y >= 0:
            x -= 1
            y -= 4
            result ^= 1

        return [ "Alice", "Bob" ][result]
