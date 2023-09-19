class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        s = sorted(nums)
        a = len(nums) - 1
        b = a // 2
        for i in range(len(s)):
            if i % 2 == 1:
                nums[i] = s[a]
                a -= 1
            else:
                nums[i] = s[b]
                b -= 1