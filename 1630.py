class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        for left, right in zip(l, r):
            if right - left < 1:
                yield False
                continue

            ok   = True
            sub  = sorted(nums[left : right + 1])
            diff = sub[1] - sub[0]
            for i in range(2, len(sub)):
                if sub[i] - sub[i - 1] != diff:
                    ok = False
                    break

            yield ok
