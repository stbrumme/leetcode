class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        candidates = []
        for r in restaurants:
            if veganFriendly == 1 and r[2] == 0:
                continue
            if maxPrice < r[3]:
                continue
            if maxDistance < r[4]:
                continue

            candidates.append(( r[1], r[0] ))

        return [ c[1] for c in sorted(candidates, reverse = True) ]
