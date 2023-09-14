class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDiv(n):
            for c in str(n):
                if c == "0":
                    return False

                if n % int(c) != 0:
                    return False
            return True

        for n in range(left, right+1):
            if isSelfDiv(n):
                yield n
