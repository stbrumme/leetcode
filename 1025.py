class Solution:
    def divisorGame(self, n: int) -> bool:
        # prime numbers always lose
        # even more interesting all odd number lose
        return (n & 1) == 0
