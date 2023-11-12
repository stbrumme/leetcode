class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            yield 0

        for i in range(1, (n // 2) + 1):
            yield +i
            yield -i
