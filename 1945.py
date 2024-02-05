class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def digitsum(x):
            result = 0
            while x > 9: # little trick to avoid modulo/div of small numbers
                result += x % 10
                x     //= 10
            return result + x

        num = ""
        abc = " abcdefghijklmnopqrstuvwxyz"
        for c in s:
            num += str(abc.index(c))

        num = int(num)
        for _ in range(k):
            num = digitsum(num)

        return num
