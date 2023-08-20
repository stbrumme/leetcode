class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num = (2**32) + num

        print(num)

        h = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" ]
        result = ""
        while num > 0:
            four = num & 15
            num >>= 4
            result = h[four] + result

        return result
