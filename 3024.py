class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a + b <= c or a + c <= b or b + c <= a:
            return "none" # invalid triangle

        size = len(set(nums))
        if size == 1:
            return "equilateral"
        if size == 2:
            return "isosceles"
        else:
            return "scalene"
