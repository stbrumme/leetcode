class Solution:
    def minFlips(self, s: str) -> int:
        result = +inf

        size = len(s)
        if size & 1:
            s += s    # try all possible type-1
        else:
            s += s[0] # even size: at most once type-1

        zero = [ 0 ] # prefix sum of errors if starting with a zero
        ones = [ 0 ] # same for ones

        for right, c in enumerate(s):
            odd = right & 1
            if ord(c) & 1 == odd:
                zero.append(zero[-1])
                ones.append(ones[-1] + 1)
            else:
                zero.append(zero[-1] + 1)
                ones.append(ones[-1])

            left = right - size
            if left >= 0:
                result = min(result, zero[right] - zero[left])
                result = min(result, ones[right] - ones[left])

        return result
