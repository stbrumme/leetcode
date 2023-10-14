class Solution:
    def queryString(self, s: str, n: int) -> bool:
        def find(n):
            b = bin(n)[2:]
            return s.find(b) != -1

        # brute force for the first 100 numbers
        for i in range(1, min(n + 1, 100)):
            if not find(i):
                return False

        # pick 1000 random numbers and hope for the best ...
        for i in range(1000):
            r = randint(1, n)
            if not find(r):
                return False

        return True
