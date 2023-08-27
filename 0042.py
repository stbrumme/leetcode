class Solution:
    def trap(self, height: List[int]) -> int:
        pivot = 0
        for h in range(len(height)):
            if height[h] > height[pivot]:
                pivot = h

        water = 0
        # left-to-pivot
        border = 0
        for h in range(pivot):
            if border > height[h]:
                water += border - height[h]
            else:
                border = height[h]

        # right-to-pivot
        border = 0
        for h in range(len(height) - 1, pivot, -1):
            if border > height[h]:
                water += border - height[h]
            else:
                border = height[h]

        return water
