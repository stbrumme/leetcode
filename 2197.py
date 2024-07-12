class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        result = [ 1 ] # not coprime with neighbors

        for n in nums:
            while   gcd(n, result[-1]) > 1: # true if coprime
                n = lcm(n, result.pop())    # reduce to their least common multiple
            result.append(n)

        return result[1 :] # skip initial [ 1 ]
