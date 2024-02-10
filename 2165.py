class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        positive = (num > 0)
        num = abs(num)

        # split into digits
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        if positive:
            digits.sort()
            for i, d in enumerate(digits):
                if d > 0: # no leading zero
                    low = [ d ] + digits[: i] + digits[i + 1 :]
                    result = 0
                    for l in low:
                        result *= 10
                        result += l
                    return result
        else:
            # negative
            result = 0
            for d in sorted(digits, reverse = True):
                result *= 10
                result += d
            return -result
