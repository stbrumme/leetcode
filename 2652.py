class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # feels like fizzbuzz :-)

        # I'm not in the mood for the mathematical approach,
        # therefore it's time for brute force (and a one-liner)
        return sum(i if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 else 0 for i in range(n + 1))
