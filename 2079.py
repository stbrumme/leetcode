class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        have   = 0
        for i, p in enumerate(plants):
            if have < p:
                result += i        # walk from the previous plant to the river
                have    = capacity # refill
                result += i        # walk back to previous (!) plant

            result += 1 # walk to current plant
            have   -= p # water it

        return result
