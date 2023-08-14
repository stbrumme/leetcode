class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        have = set()
        for i in candyType:
            have.add(i)

        variety = len(candyType)
        return min(variety // 2, len(have))
