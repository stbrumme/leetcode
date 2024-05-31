class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # all bits can be treated separately,
        # therefore let's define the uppercase letters I, J, K
        # to be a single bit (at the same position) of i, j, k
        # if K == 0 then (I | J) & K == 0
        # and of course x ^ 0 == 0

        # that means only K == 1 affects the result
        # so that only I | J is left

        # if we consider all (!) combinations of nums[i], nums[j]
        # then we have I | J as well as J | I
        # since I | J == J | I and x ^ x == 0
        # all these combinations cancel each other and
        # our overall result seems to be zero

        # however, the indices can be identical, too:
        # more precisely (nums[i], nums[i], nums[k]) is a valid triple
        # notice the second index is i instead of the usual j
        # for these numbers we have I | I == I => but only once

        # in the end exactly these triples (I, I, ) influence the result
        # since they are the only ones who aren't zero and/or cancel each other

        # finally the equation gets simplified: (I | J) & K == I

        x = 0
        for n in nums:
            x ^= n
        return x

        # on a personal note:
        # I hate these problems where almost no coding is involved
        # the website is called leetcode, not leetmath
