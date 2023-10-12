class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        consumed = 0
        refuel   = 5
        while mainTank >= refuel:
            mainTank -= refuel
            consumed += refuel
            if additionalTank > 0:
                additionalTank -= 1
                mainTank       += 1

        consumed += mainTank
        return consumed * 10
