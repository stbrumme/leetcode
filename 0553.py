class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # not at lot of programming but needs some math understanding:
        # we want to maximize a/b
        # a is max if it's a sole number
        # b is min if it's divided many times

        s = [ str(n) for n in nums ]

        if len(nums) == 1:
            return s[0]

        if len(nums) == 2:
            return "/".join(s)

        return s[0] + "/(" + "/".join(s[1:]) + ")"
