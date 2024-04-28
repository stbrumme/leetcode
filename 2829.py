class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        result = 0

        skip = set()
        have = 0
        for i in count(1):
            if i not in skip:
                # disallow pair
                if k > i:
                    skip.add(k - i)

                # accept number
                result += i
                have   += 1
                # enough
                if have == n:
                    return result
