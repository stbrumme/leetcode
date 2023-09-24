class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        for digits in range(2, 10):
            for start in range(9 - digits + 1):
                check = int("123456789"[start:digits+start])
                if low <= check <= high:
                    yield check