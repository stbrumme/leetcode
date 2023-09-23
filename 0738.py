class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        result = 0

        def deeper(have):
            if have > s:
                return False

            if len(have) == len(s):
                nonlocal result
                result = int(have)
                return True

            last = 0 if not have else int(have[-1])
            for i in range(9, last-1, -1):
                if deeper(have + str(i)):
                    return True
            return False
        
        deeper("")
        return result