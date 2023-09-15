class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t = tomatoSlices
        c = cheeseSlices

        if t > 4*c or t < 2*c or t % 2 == 1:
            return []

        # try only small
        small = c
        t -= 2*small
        # need jumbos
        jumbo  = t // 2
        # instead of small
        small -= jumbo
        return [ jumbo, small ]
