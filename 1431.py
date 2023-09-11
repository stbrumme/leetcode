class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [ i + extraCandies >= max(candies) for i in candies ]
