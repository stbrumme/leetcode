class Solution:
    def minimumSum(self, num: int) -> int:
        result = 9999
        for p in permutations(str(num)):
            pp = "".join(p)
            result = min(result, int(pp[:1]) + int(pp[1:]))
            result = min(result, int(pp[:2]) + int(pp[2:]))
            result = min(result, int(pp[:3]) + int(pp[3:]))
        return result
